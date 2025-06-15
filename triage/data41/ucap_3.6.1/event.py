from __future__ import annotations

from typing import TYPE_CHECKING, Any, Sequence

if TYPE_CHECKING:
    from .fail_safe_parameter_value import FailSafeParameterValue
    from .value_type import ValueType
from .selectors import Selector


class Event:
    """
    Represents a UCAP event, which contains the latest values for all input streams.

    Events can be built every time an input signal is received, or when certain conditions are met, e.g. when a new
    cycle stamp is received or when a specified trigger signal is received.

    See <a href="https://wikis.cern.ch/display/UCAP/Event+Building">event building UCAP wiki</a> for more details.

    Inputs can optionally be buffered, in which case the event holds the N latest values for the given input otherwise
    the event only contains the latest value received.

    Calling getters on input for which there is no value returns `None`.

    Note that methods do not copy the data itself.
    """

    # Docstring based on the Java counterpart
    # This class is simply a data wrapper for the response, not a counterpart implementation of the Java Event

    def __init__(self):
        """Constructor. Objects shall be constructed by either the Python transformation server or test utilities."""
        # this is int64 in for seconds and int32 for nanos (as fraction of a second) in protobuf
        self._creation_time: float = None
        self._trigger_name: str | None = None
        self._trigger_value: FailSafeParameterValue | None = None
        self._value_names: tuple[str, ...] = None
        self._missing_value_names: tuple[str, ...] = None
        self._all_buffered_values: dict[
            str, Sequence[FailSafeParameterValue]
        ] = None
        self._timeout_reached: bool = None

    ############################################################################
    ### METADATA ###############################################################
    ############################################################################

    @property
    def creation_time(self) -> float:
        """
        Represents the time of creation of this Event object.
        This returns a float where integer part represents seconds, while the fractional part represents
        nanoseconds (as fraction of a second)

        Returns
        -------
        float
            representing the creation time.

        """
        return self._creation_time

    @property
    def event_creation_time(self) -> float:
        """
        DEPRECATED: Use #creation_time instead.

        Represents the time of creation of this Event object.
        This returns a float where integer part represents seconds, while the fractional part represents
        nanoseconds (as fraction of a second)

        Returns
        -------
        float
            representing the event creation time.

        """
        return self._creation_time

    @property
    def timeout_reached(self) -> bool:
        """
        Indicates whether the Event was sent after the timeout for trigger signal has been reached.

        Returns
        -------
        bool
            True if timeout was reached, False otherwise

        """
        return self._timeout_reached

    ############################################################################
    ### ALIASES ################################################################
    ############################################################################

    @property
    def error_value_names(self) -> tuple[str, ...]:
        """
        Returns all aliases for which an error is present.

        For buffered values it checks all values present in the buffer and returns the name of the value if it has
        any errors.

        Returns
        -------
        tuple[str]
            a tuple containing a tuple of parameter names for which an error is present

        """
        error_value_names: set[str] = set()

        for value_name in self.value_names:
            for value in self.get_values(value_name):
                if value and value.exception:
                    error_value_names.add(value_name)

        return tuple(sorted(error_value_names))

    @property
    def missing_value_names(self) -> tuple[str, ...]:
        """
        Returns all aliases for which no value is present.

        For buffered values it checks whether any value is present.

        Returns
        -------
        tuple[str]
            a tuple containing a tuple of parameter names which didn't acquire any data when
            this Event object was created.

        """
        return self._missing_value_names

    @property
    def trigger_name(self) -> str | None:
        """
        Stores the name of the parameter that triggered the creation of this Event object.

        Returns
        -------
        str
            name of the parameter that was responsible for creating this Event object.

        """
        return self._trigger_name

    @property
    def value_names(self) -> tuple[str, ...]:
        """
        Return a tuple containing names of all parameters for which values have been acquired for this Event object.

        Returns
        -------
        tuple[str]
            tuple of parameter names for which values have been recorded in this Event.

        """
        return self._value_names

    ############################################################################
    ### DATA FSPV ##############################################################
    ############################################################################

    @property
    def trigger_value(self) -> FailSafeParameterValue | None:
        """
        Returns the acquired data associated with the parameter that triggered the creation of this Event object.

        Returns
        -------
        Optional[FailSafeParameterValue]
            fspv containing the data associated with the parameter responsible for creating this Event object.

        """
        return self._trigger_value

    def get_value(self, param_name: str) -> FailSafeParameterValue | None:
        """
        Returns the FailSafeParameterValue object for the value acquired from the given parameter.
        In case values of the given parameter were buffered - the most recent one will be returned.

        Parameters
        ----------
        param_name : str
            the name of the parameter for which the value was acquired.

        Returns
        -------
        Optional[FailSafeParameterValue]
            object containing acquisition data of the parameter, or None if the data for it was expected,
            but was not recorded in this event (param_name is in #missing_value_names)

        """
        fspvs = self._all_buffered_values.get(param_name)
        if fspvs:
            return fspvs[-1]
        return None

    def get_value_by_selector(
        self, param_name: str, selector: Selector | str
    ) -> FailSafeParameterValue | None:
        """
        Returns the FailSafeParameterValue object for the value acquired from the given parameter and user selector.

        This method should be only used for subscriptions declared in the bufferedBySelectorSubscriptions block.

        Parameters
        ----------
        param_name : str
            the name of the parameter for which the value was acquired.
        selector   : Union[Selector, str]
            the user selector for which the value was acquired.

        Returns
        -------
        Optional[FailSafeParameterValue]
            object containing acquisition data of the parameter and user selector, or None if the data for it was expected,
            but was not recorded in this event (param_name@selector is in #missing_value_names)

        """
        selector_alias: str = self._convert_alias_to_selector_alias(
            param_name, selector
        )

        return self.get_value(selector_alias)

    def get_values(self, param_name: str) -> tuple[FailSafeParameterValue, ...]:
        """
        Returns a tuple containing all FailSafeParameterValue objects acquired from the given parameter.
        The values are returned in ascending date order, meaning that the first element of the tuple
        is the oldest value, while the last one is the newest.

        Parameters
        ----------
        param_name : str
            the name of the parameter for which values were acquired.

        Returns
        -------
        tuple[FailSafeParameterValue, ...]
            tuple containing acquisition data of the parameter, or empty tuple if the data for it was expected,
            but was not recorded in this event (param_name is in #missing_value_names)

        """
        if param_name in self._all_buffered_values:
            return tuple(self._all_buffered_values[param_name])
        return ()

    def get_values_by_selector(
        self, param_name: str, selector: Selector | str
    ) -> tuple[FailSafeParameterValue, ...]:
        """
        Returns a tuple containing all FailSafeParameterValue objects acquired from the given parameter and user selector.
        The values are returned in ascending date order, meaning that the first element of the tuple
        is the oldest value, while the last one is the newest.

        This method should be only used for subscriptions declared in the bufferedBySelectorSubscriptions block.

        Parameters
        ----------
        param_name : str
            the name of the parameter for which values were acquired.
        selector   : Union[Selector, str]
            the user selector for which for which values were acquired.

        Returns
        -------
        tuple[FailSafeParameterValue, ...]
            tuple containing acquisition data of the parameter and user selector, or empty tuple if the data for it was expected,
            but was not recorded in this event (param_name@selector is in #missing_value_names)

        """
        selector_alias: str = Event._convert_alias_to_selector_alias(
            param_name, selector
        )

        return self.get_values(selector_alias)

    ############################################################################
    ### DATA PLAIN #############################################################
    ############################################################################

    def get_plain_value(
        self, param_name: str, field_name: str = "value"
    ) -> Any:
        """
        Returns the actual value of a particular field of given parameter.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        Parameters
        ----------
        param_name : str
            The name of the parameter of which the value should be retrieved.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        Any
            the actual value of the field

        """
        return self.get_plain_value_and_type(param_name, field_name)[0]

    def get_plain_value_by_selector(
        self,
        param_name: str,
        selector: Selector | str,
        field_name: str = "value",
    ) -> Any:
        """
        Returns the actual value of a particular field of given parameter and user selector.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        This method should be only used for subscriptions declared in the bufferedBySelectorSubscriptions block.

        Parameters
        ----------
        param_name : str
            The name of the parameter of which the value should be retrieved.
        selector   : Union[Selector, str]
            the user selector of which the value should be retrieved.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        Any
            the actual value of the field

        """
        selector_alias: str = self._convert_alias_to_selector_alias(
            param_name, selector
        )

        return self.get_plain_value(selector_alias, field_name)

    def get_plain_value_and_type(
        self, param_name: str, field_name: str = "value"
    ) -> tuple[Any, ValueType] | tuple[None, None]:
        """
        Returns the actual value of a particular field of given parameter as well as its value type.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        In case values of the given parameter were buffered - the most recent one will be returned.

        Parameters
        ----------
        param_name : str
            The name of the parameter of which the value should be retrieved.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        Union[tuple[Any, str], tuple[None, None]]
            tuple containing the actual value as the first element, and a string describing the value type as
            the second one

        Raises
        ------
        ValueError
            if the parameter value is present, but the provided field name was not defined

        """
        fspv = self.get_value(param_name)
        if fspv and fspv.value:
            return fspv.value.get_value_and_type(field_name)
        return None, None

    def get_plain_value_and_type_by_selector(
        self,
        param_name: str,
        selector: Selector | str,
        field_name: str = "value",
    ) -> tuple[Any, ValueType] | tuple[None, None]:
        """
        Returns the actual value of a particular field of given parameter and user selector as well as its value type.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        This method should be only used for subscriptions declared in the bufferedBySelectorSubscriptions block.

        Parameters
        ----------
        param_name : str
            The name of the parameter of which the value should be retrieved.
        selector   : Union[Selector, str]
            The user selector of which the value should be retrieved.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        Union[tuple[Any, str], tuple[None, None]]
            tuple containing the actual value as the first element, and a string describing the value type as
            the second one

        Raises
        ------
        ValueError
            if the value for given parameter and user selector is present, but the provided field name was not defined

        """
        selector_alias: str = self._convert_alias_to_selector_alias(
            param_name, selector
        )

        return self.get_plain_value_and_type(selector_alias, field_name)

    def get_plain_values(
        self, param_name: str, field_name: str = "value"
    ) -> tuple[Any, ...]:
        """
        Returns a tuple of actual values of a particular field of given parameter.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        The values are returned in ascending date order, meaning that the first element of the tuple
        is the oldest value, while the last one is the newest.

        Parameters
        ----------
        param_name : str
            The name of the parameter for which values were acquired.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        tuple[Any, ...]
            tuple of the actual values acquired for the parameter

        """
        values_and_types = self.get_plain_values_and_types(
            param_name, field_name
        )
        if values_and_types:
            return tuple(value[0] for value in values_and_types)
        return ()

    def get_plain_values_by_selector(
        self,
        param_name: str,
        selector: Selector | str,
        field_name: str = "value",
    ) -> tuple[Any, ...]:
        """
        Returns a tuple of actual values of a particular field of given parameter and user selector.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        The values are returned in ascending date order, meaning that the first element of the tuple
        is the oldest value, while the last one is the newest.

        This method should be only used for subscriptions declared in the bufferedBySelectorSubscriptions block.

        Parameters
        ----------
        param_name : str
            The name of the parameter for which values were acquired.
        selector   : Union[Selector, str]
            The user selector for which values were acquired.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        tuple[Any, ...]
            tuple of the actual values acquired for the given parameter and user selector

        """
        selector_alias: str = self._convert_alias_to_selector_alias(
            param_name, selector
        )

        return self.get_plain_values(selector_alias, field_name)

    def get_plain_values_and_types(
        self, param_name: str, field_name: str = "value"
    ) -> tuple[tuple[Any, ValueType] | tuple[None, None], ...]:
        """
        Returns a tuple of tuples containing actual values of a particular field of given parameter as well as their
        corresponding values types.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        The values are returned in ascending date order, meaning that the first element of the tuple
        is the oldest value, while the last one is the newest.

        Parameters
        ----------
        param_name : str
            The name of the parameter for which values were acquired.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        tuple[Union[tuple[Any, ValueType], tuple[None, None]], ...]
            tuple of tuples containing the actual value as the first element, and a string describing the value type as
            the second one

        Raises
        ------
        ValueError
           if the parameter value is present, but the provided field name was not defined

        """
        fspv_values: tuple[FailSafeParameterValue, ...] = self.get_values(
            param_name
        )

        unpacked_values: list[tuple[Any, ValueType] | tuple[None, None]] = []
        for fspv in fspv_values:
            if fspv.value:
                unpacked_values.append(
                    fspv.value.get_value_and_type(field_name)
                )
            else:
                unpacked_values.append((None, None))

        return tuple(unpacked_values)

    def get_plain_values_and_types_by_selector(
        self,
        param_name: str,
        selector: Selector | str,
        field_name: str = "value",
    ) -> tuple[tuple[Any, ValueType] | tuple[None, None], ...]:
        """
        Returns a tuple of tuples containing actual values of a particular field of given parameter and user selector as well as their
        corresponding values types.

        This means that the method actually hides all the value unpacking
        (FailSafeParameterValue -> AcquiredParameterValue -> actual_value),
        with the risk that it may throw an exception if the data for the given field is not there.

        The values are returned in ascending date order, meaning that the first element of the tuple
        is the oldest value, while the last one is the newest.

        This method should be only used for subscriptions declared in the bufferedBySelectorSubscriptions block.

        Parameters
        ----------
        param_name : str
            The name of the parameter for which values were acquired.
        selector   : Union[Selector, str]
            The user selector for which values were acquired.
        field_name : str, optional
            The name of the field of the property of which the value should be retrieved.
            If not specified it is assumed that the subscription was defined directly to the field itself,
            by default "value"

        Returns
        -------
        tuple[Union[tuple[Any, ValueType], tuple[None, None]], ...]
            tuple of tuples containing the actual value as the first element, and a string describing the value type as
            the second one

        Raises
        ------
        ValueError
           if the value is present for given parameter and selector, but the provided field name was not defined

        """
        selector_alias: str = self._convert_alias_to_selector_alias(
            param_name, selector
        )

        return self.get_plain_values_and_types(selector_alias, field_name)

    ############################################################################
    ### TO STRING ##############################################################
    ############################################################################

    def __repr__(self) -> str:
        return (
            f"Event(\n"
            f"\tevent_creation_time={self.event_creation_time}\n"
            f"\ttimeout_reached={self.timeout_reached}\n"
            f"\tvalue_names={self.value_names}\n"
            f"\terror_value_names={self.error_value_names}\n"
            f"\tmissing_value_names={self.missing_value_names}\n"
            f"\ttrigger_name={self.trigger_name}\n"
            f"\ttrigger_value={self.trigger_value}\n"
            f"\tall_buffered_values={self._all_buffered_values}\n"
            f")"
        )

    ############################################################################
    ### INTERNAL ###############################################################
    ############################################################################

    @staticmethod
    def _convert_alias_to_selector_alias(
        value_name: str, selector: str | Selector
    ) -> str:
        """
        Converts given alias and selector to an alias formatted as value_name@selector.

        Parameters
        ----------
        value_name : str
            the alias to be converted
        selector   : str, Selector
            the selector to be converted

        Returns
        -------
        str
            The combined alias and user selector as value_name@selector

        """
        if not value_name:
            raise ValueError(f"Invalid value_name: {value_name}")

        if isinstance(selector, str):
            selector_id = selector
        elif isinstance(selector, Selector):
            selector_id = selector.selector_id
        else:
            raise ValueError(f"Invalid selector: {selector}")  # noqa: TRY004

        return f"{value_name}@{selector_id}"
