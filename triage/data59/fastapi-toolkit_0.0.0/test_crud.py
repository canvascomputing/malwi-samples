from unittest.mock import MagicMock

import pytest
from sqlalchemy import (
    desc,
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_toolkit.crud.base import CRUDBase
from tests.mixer import AsyncMixer
from tests.models import Book
from tests.schemas import (
    BookSchema,
    BookSchemaCreate,
)


class TestCRUDGet:
    async def test_one__ok(self, mixer: AsyncMixer):
        test_book = await mixer.blend(Book)
        book = await CRUDBase(Book).get(Book.title == test_book.title)
        assert BookSchema.from_orm(book) == BookSchema.from_orm(test_book)

    async def test_no_one__ok(self, mixer: AsyncMixer):
        await mixer.blend(Book, title='some_title')
        book = await CRUDBase(Book).get(Book.title == 'wrong_title')
        assert book is None


class TestCRUDCount:
    async def test_count__ok(self, mixer: AsyncMixer):
        test_count = 3
        await mixer.cycle(test_count).blend(Book)
        count = await CRUDBase(Book).count()
        assert count == test_count

    async def test_count_with_filter__ok(self, mixer: AsyncMixer):
        test_count = 3
        await mixer.cycle(test_count).blend(
            Book,
            title=mixer.sequence('Title_{0}'),
            page_amount=mixer.sequence()
        )
        count = await CRUDBase(Book).count((Book.title == 'Title_1', ))
        assert count == 1


class TestCRUDGetModelId:
    def test__ok(self):
        id_mock = MagicMock()
        model_mock = MagicMock(id=id_mock)
        crud = CRUDBase(model_mock)
        assert crud.get_model_id() is id_mock


class TestCRUDList:
    async def test__ok(self, mixer: AsyncMixer):
        test_count = 3
        test_books = await mixer.cycle(test_count).blend(Book)
        books, count = await CRUDBase(Book).list()

        assert count == test_count
        for book, test_book in zip(
            sorted(books, key=lambda x: x.id), test_books
        ):
            assert BookSchema.from_orm(book) == BookSchema.from_orm(test_book)

    async def test_empty_list__ok(self, mixer: AsyncMixer):
        books, count = await CRUDBase(Book).list()
        assert list(books) == []
        assert count == 0

    async def test_offset__ok(self, mixer: AsyncMixer):
        test_count = 3
        await mixer.cycle(test_count).blend(Book)
        books, count = await CRUDBase(Book).list(offset=1)
        assert len(list(books)) == 2
        assert count == test_count

    async def test_limit__ok(self, mixer: AsyncMixer):
        test_count = 3
        await mixer.cycle(test_count).blend(Book)
        books, count = await CRUDBase(Book).list(limit=2)
        assert len(list(books)) == 2
        assert count == test_count

    async def test_filter_query__ok(self, mixer: AsyncMixer):
        test_count = 3
        test_books = await mixer.cycle(test_count).blend(
            Book,
            title=mixer.sequence('Title_{0}'),
        )
        books, count = await CRUDBase(Book).list(
            filter_query=(Book.title == 'Title_1', )
        )
        assert count == 1
        assert BookSchema.from_orm(list(books)[0]) == BookSchema.from_orm(
            test_books[1]
        )

    async def test_estimated_count_false__ok(self, mixer: AsyncMixer):
        await mixer.cycle(3).blend(Book)
        _, count = await CRUDBase(Book).list(estimate_count=False)

        assert count is None

    async def test_order_by__ok(self, mixer: AsyncMixer):
        test_count = 3
        test_books = await mixer.cycle(test_count).blend(
            Book,
            page_amount=mixer.sequence(7, 3, 4),
        )
        books, count = await CRUDBase(Book).list(order_by=(Book.page_amount, ))

        assert count == test_count
        for book, test_book in zip(
            books, sorted(test_books, key=lambda x: x.page_amount)
        ):
            assert BookSchema.from_orm(book) == BookSchema.from_orm(test_book)

    async def test_multiple_params__ok(self, mixer: AsyncMixer):
        test_count = 6
        test_books = await mixer.cycle(test_count).blend(
            Book,
            page_amount=mixer.sequence(7, 3, 4, 5, 9, 10),
        )
        books, count = await CRUDBase(Book).list(
            filter_query=(Book.page_amount > 4, ),
            limit=1,
            offset=1,
            order_by=(desc(Book.page_amount), )
        )
        books_list = list(books)
        assert count == 4
        assert len(books_list) == 1
        assert BookSchema.from_orm(books_list[0]) == BookSchema.from_orm(
            test_books[-2]
        )


class TestCRUDCreate:
    @pytest.mark.parametrize(
        ('args', 'kwargs'),
        [
            ((BookSchemaCreate(title='test_title', page_amount=5), ), {}, ),
            ((BookSchemaCreate(title='test_title'), {'page_amount': 5}), {}, ),
            ((), {'title': 'test_title', 'page_amount': 5}, )
        ]
    )
    async def test__ok(
            self, args, kwargs, session: AsyncSession
    ):
        result = await CRUDBase(Book).create(*args, **kwargs)
        book_from_db = (await session.execute(select(Book))).scalars().first()
        test_result = {
            'title': 'test_title', 'page_amount': 5, 'id': book_from_db.id
        }
        assert BookSchema.from_orm(result) == BookSchema.from_orm(book_from_db)
        assert BookSchema.from_orm(result) == BookSchema(**test_result)


class TestCRUDUpdate:
    async def test_db_obj__ok(self, mixer: AsyncMixer):
        init_book = await mixer.blend(Book, title='title', page_amount=5)
        test_title = 'new_title'
        init_book.title = test_title

        new_book = await CRUDBase(Book).update(
            init_book, session=mixer.session
        )
        book_from_db = (
            await mixer.session.execute(select(Book))
        ).scalars().first()

        assert BookSchema.from_orm(new_book) == BookSchema.from_orm(
            book_from_db
        )
        assert BookSchema.from_orm(new_book) == BookSchema(
            id=book_from_db.id,
            title=test_title,
            page_amount=5
        )

    async def test_obj_in__ok(self, mixer: AsyncMixer):
        init_book = await mixer.blend(Book, title='title', page_amount=5)
        test_title = 'new_title'
        obj_in = BookSchemaCreate(title=test_title)
        new_book = await CRUDBase(Book).update(
            init_book, obj_in, session=mixer.session
        )
        book_from_db = (
            await mixer.session.execute(select(Book))
        ).scalars().first()
        assert BookSchema.from_orm(new_book) == BookSchema.from_orm(
            book_from_db
        )
        assert BookSchema.from_orm(new_book) == BookSchema(
            id=book_from_db.id,
            title=test_title,
            page_amount=5
        )

    async def test_data__ok(self, mixer: AsyncMixer):
        init_book = await mixer.blend(Book, title='title', page_amount=5)
        test_title = 'new_title'
        data = {'title': test_title}
        new_book = await CRUDBase(Book).update(
            init_book, session=mixer.session, **data
        )
        book_from_db = (
            await mixer.session.execute(select(Book))
        ).scalars().first()
        assert BookSchema.from_orm(new_book) == BookSchema.from_orm(
            book_from_db
        )
        assert BookSchema.from_orm(new_book) == BookSchema(
            id=book_from_db.id,
            title=test_title,
            page_amount=5
        )


class TestCRUDDelete:
    async def test__ok(self, mixer: AsyncMixer):
        book_1, book_2 = await mixer.cycle(2).blend(Book)
        await CRUDBase(Book).delete(Book.id == book_2.id)
        books_from_db = (await mixer.session.execute(select(Book))).scalars()
        books_from_db_list = list(books_from_db)
        assert len(books_from_db_list) == 1
        assert BookSchema.from_orm(book_1) == BookSchema.from_orm(
            books_from_db_list[0]
        )


class TestCRUDGetOrCreate:
    async def test_create__ok(self, session: AsyncSession):
        test_title = 'test_title'
        defaults = {
            'title': test_title,
            'page_amount': 5,
        }
        result, created = await CRUDBase(Book).get_or_create(
            Book.title == test_title, **defaults
        )
        book_from_db = (await session.execute(select(Book))).scalars().first()
        test_result = {
            'id': book_from_db.id,
            **defaults
        }
        assert BookSchema.from_orm(result) == BookSchema.from_orm(book_from_db)
        assert BookSchema.from_orm(result) == BookSchema(**test_result)
        assert created is True

    async def test_get__ok(self, mixer: AsyncMixer):
        test_title = 'test_title'
        defaults = {
            'title': test_title,
            'page_amount': 5,
        }
        await mixer.blend(Book, **defaults)
        result, created = await CRUDBase(Book).get_or_create(
            Book.title == test_title, **defaults
        )
        book_from_db = (
            await mixer.session.execute(select(Book))
        ).scalars().first()
        test_result = {
            'id': book_from_db.id,
            **defaults
        }
        assert BookSchema.from_orm(result) == BookSchema.from_orm(book_from_db)
        assert BookSchema.from_orm(result) == BookSchema(**test_result)
        assert created is False
