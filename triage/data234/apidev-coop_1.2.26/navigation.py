# -*- coding: utf-8 -*-
"""navigation: the navigation tree page"""

import json

from django.db.models.aggregates import Max
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError, PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import select_template
from django.utils.translation import ugettext as _

from coop_cms import models
from coop_cms.settings import get_navtree_class
from coop_cms.logger import logger
from coop_cms.utils import get_model_app, get_model_label, get_model_name


def view_navnode(request, tree):
    """show info about the node when selected"""
    try:
        response = {}

        node_id = request.POST['node_id']
        node = models.NavNode.objects.get(tree=tree, id=node_id)
        model_name = object_label = ""

        # get the admin url
        if node.content_type:
            app, mod = node.content_type.app_label, node.content_type.model
            admin_url = reverse("admin:{0}_{1}_change".format(app, mod), args=(node.object_id,))

            # load and render template for the object
            # try to load the corresponding template and if not found use the default one
            model_name = u"{0}".format(node.content_type)
            object_label = u"{0}".format(node.content_object)
            template = select_template([
                "coop_cms/navtree_content/{0}.html".format(node.content_type.name),
                "coop_cms/navtree_content/default.html"
            ])
        else:
            admin_url = u""
            template = select_template(["coop_cms/navtree_content/default.html"])

        html = template.render(
            RequestContext(
                request,
                {
                    "node": node,
                    "admin_url": admin_url,
                    "model_name": model_name,
                    "object_label": object_label,
                }
            )
        )

        # return data has dictionnary
        response['html'] = html
        response['message'] = u"Node content loaded."

        return response
    except Exception:
        logger.exception("view_navnode")
        raise


def rename_navnode(request, tree):
    """change the name of a node when renamed in the tree"""
    response = {}
    node_id = request.POST['node_id']
    node = models.NavNode.objects.get(tree=tree, id=node_id)  # get the node
    old_name = node.label  # get the old name for success message
    node.label = request.POST['name']  # change the name
    node.save()
    if old_name != node.label:
        response['message'] = _(u"The node '{0}' has been renamed into '{1}'.").format(old_name, node.label)
    else:
        response['message'] = ''
    return response


def remove_navnode(request, tree):
    """delete a node"""
    # Keep multi node processing even if multi select is not allowed
    response = {}
    node_ids = request.POST['node_ids'].split(";")
    for node_id in node_ids:
        models.NavNode.objects.get(tree=tree, id=node_id).delete()
    if len(node_ids) == 1:
        response['message'] = _(u"The node has been removed.")
    else:
        response['message'] = _(u"{0} nodes has been removed.").format(len(node_ids))
    return response


def move_navnode(request, tree):
    """move a node in the tree"""
    response = {}

    node_id = request.POST['node_id']
    ref_pos = request.POST['ref_pos']
    parent_id = request.POST.get('parent_id', 0)
    ref_id = request.POST.get('ref_id', 0)

    node = models.NavNode.objects.get(tree=tree, id=node_id)

    if parent_id:
        sibling_nodes = models.NavNode.objects.filter(tree=tree, parent__id=parent_id)
        parent_node = models.NavNode.objects.get(tree=tree, id=parent_id)
    else:
        sibling_nodes = models.NavNode.objects.filter(tree=tree, parent__isnull=True)
        parent_node = None

    if ref_id:
        ref_node = models.NavNode.objects.get(tree=tree, id=ref_id)
    else:
        ref_node = None

    # Update parent if changed
    if parent_node != node.parent:
        if node.parent:
            ex_siblings = models.NavNode.objects.filter(tree=tree, parent=node.parent).exclude(id=node.id)
        else:
            ex_siblings = models.NavNode.objects.filter(tree=tree, parent__isnull=True).exclude(id=node.id)

        node.parent = parent_node

        # restore ex-siblings
        for sib_node in ex_siblings.filter(ordering__gt=node.ordering):
            sib_node.ordering -= 1
            sib_node.save()

        # move siblings if inserted
        if ref_node:
            if ref_pos == "before":
                to_be_moved = sibling_nodes.filter(ordering__gte=ref_node.ordering)
                node.ordering = ref_node.ordering
            elif ref_pos == "after":
                to_be_moved = sibling_nodes.filter(ordering__gt=ref_node.ordering)
                node.ordering = ref_node.ordering + 1
            for ntbm in to_be_moved:
                ntbm.ordering += 1
                ntbm.save()

        else:
            # add at the end
            max_ordering = sibling_nodes.aggregate(max_ordering=Max('ordering'))['max_ordering'] or 0
            node.ordering = max_ordering + 1

    else:

        # Update pos if changed
        if ref_node:
            if ref_node.ordering > node.ordering:
                # move forward
                to_be_moved = sibling_nodes.filter(ordering__lt=ref_node.ordering, ordering__gt=node.ordering)
                for next_sibling_node in to_be_moved:
                    next_sibling_node.ordering -= 1
                    next_sibling_node.save()

                if ref_pos == "before":
                    node.ordering = ref_node.ordering - 1

                elif ref_pos == "after":
                    node.ordering = ref_node.ordering - 1

            elif ref_node.ordering < node.ordering:
                # move backward
                to_be_moved = sibling_nodes.filter(ordering__gt=ref_node.ordering, ordering__lt=node.ordering)
                for next_sibling_node in to_be_moved:
                    next_sibling_node.ordering += 1
                    next_sibling_node.save()

                if ref_pos == "before":
                    node.ordering = ref_node.ordering
                    ref_node.ordering += 1
                    ref_node.save()
                elif ref_pos == "after":
                    node.ordering = ref_node.ordering + 1

        else:
            max_ordering = sibling_nodes.aggregate(max_ordering=Max('ordering'))['max_ordering'] or 0
            node.ordering = max_ordering + 1

    node.save()
    response['message'] = _(u"The node '{0}' has been moved.").format(node.label)

    return response


def add_navnode(request, tree):
    """Add a new node"""
    response = {}

    # get the type of object
    object_type = request.POST['object_type']
    if object_type:
        app_label, model_name = object_type.split('.')
        content_type = ContentType.objects.get(app_label=app_label, model=model_name)
        model_class = content_type.model_class()
        object_id = request.POST['object_id']
        model_name = get_model_label(model_class)
        if not object_id:
            raise ValidationError(_(u"Please choose an existing {0}").format(model_name.lower()))
        try:
            obj = model_class.objects.get(id=object_id)
        except model_class.DoesNotExist:
            raise ValidationError(_(u"{0} {1} not found").format(get_model_label(model_class), object_id))

        # objects can not be added twice in the navigation tree
        if models.NavNode.objects.filter(tree=tree, content_type=content_type, object_id=obj.id).count() > 0:
            raise ValidationError(_(u"The {0} is already in navigation").format(get_model_label(model_class)))

    else:
        content_type = None
        obj = None

    # Create the node
    parent_id = request.POST.get('parent_id', 0)
    if parent_id:
        parent = models.NavNode.objects.get(tree=tree, id=parent_id)
    else:
        parent = None
    node = models.create_navigation_node(content_type, obj, tree, parent)

    response['label'] = node.label
    response['id'] = 'node_{0}'.format(node.id)
    response['message'] = _(u"'{0}' has added to the navigation tree.").format(node.label)

    return response


def get_suggest_list(request, tree):
    """call by auto-complete"""
    response = {}
    suggestions = []
    term = request.POST["term"]  # the 1st chars entered in the autocomplete

    if tree.types.count() == 0:
        nav_types = models.NavType.objects.all()
    else:
        nav_types = tree.types.all()

    for nav_type in nav_types:
        content_type = nav_type.content_type
        if nav_type.label_rule == models.NavType.LABEL_USE_SEARCH_FIELD:
            # Get the name of the default field for the current type (eg: Page->title, Url->url ...)
            lookup = {nav_type.search_field + '__icontains': term}
            objects = content_type.model_class().objects.filter(**lookup)
        elif nav_type.label_rule == models.NavType.LABEL_USE_GET_LABEL:
            objects = [
                obj for obj in content_type.model_class().objects.all() if term.lower() in obj.get_label().lower()
            ]
        else:
            objects = [
                obj for obj in content_type.model_class().objects.all() if term.lower() in unicode(obj).lower()
            ]

        already_in_navigation = [
            node.object_id for node in models.NavNode.objects.filter(tree=tree, content_type=content_type)
        ]

        # Get suggestions as a list of {label: object.get_label() or unicode if no get_label, 'value':<object.id>}
        for obj in objects:
            if obj.id not in already_in_navigation:
                # Suggest only articles which are not in navigation yet
                suggestions.append({
                    'label': models.get_object_label(content_type, obj),
                    'value': obj.id,
                    'category': get_model_label(content_type.model_class()).capitalize(),
                    'type': content_type.app_label + u'.' + content_type.model,
                })

    # Add suggestion for an empty node
    suggestions.append({
        'label': _(u"Node"),
        'value': 0,
        'category': _(u"Empty node"),
        'type': "",
    })
    response['suggestions'] = suggestions
    return response


def navnode_in_navigation(request, tree):
    """toogle the is_visible_flag of a navnode"""
    response = {}
    node_id = request.POST['node_id']
    node = models.NavNode.objects.get(tree=tree, id=node_id)  # get the node
    node.in_navigation = not node.in_navigation
    node.save()
    if node.in_navigation:
        response['message'] = _(u"The node is now visible.")
        response['label'] = _(u"Hide node in navigation")
        response['icon'] = "in_nav"
    else:
        response['message'] = _(u"The node is now hidden.")
        response['label'] = _(u"Show node in navigation")
        response['icon'] = "out_nav"
    return response


@login_required
def process_nav_edition(request, tree_id):
    """This handle ajax request sent by the tree component"""
    if request.method == 'POST' and request.is_ajax() and 'msg_id' in request.POST:
        try:
            # Get the current tree
            tree_class = get_navtree_class()
            tree = get_object_or_404(tree_class, id=tree_id)

            # check permissions
            perm_name = "{0}.change_{1}".format(get_model_app(tree_class), get_model_name(tree_class))
            if not request.user.has_perm(perm_name):
                raise PermissionDenied

            functions = (
                view_navnode, rename_navnode, remove_navnode, move_navnode,
                add_navnode, get_suggest_list, navnode_in_navigation,
            )
            supported_msg = {}
            # create a map between message name and handler
            # use the function name as message id
            for fct in functions:
                supported_msg[fct.__name__] = fct

            # Call the handler corresponding to the requested message
            response = supported_msg[request.POST['msg_id']](request, tree)

            # If no exception raise: Success
            response['status'] = 'success'
            response.setdefault('message', 'Ok')  # if no message defined in response, add something

        except KeyError as msg:
            response = {'status': 'error', 'message': u"Unsupported message : {0}".format(msg)}
        except PermissionDenied:
            response = {'status': 'error', 'message': u"You are not allowed to add a node"}
        except ValidationError as ex:
            response = {'status': 'error', 'message': u' - '.join(ex.messages)}
        except Exception as msg:
            logger.exception("process_nav_edition")
            response = {'status': 'error', 'message': u"An error occured : {0}".format(msg)}

        # return the result as json object
        return HttpResponse(json.dumps(response), content_type='application/json')
    raise Http404

