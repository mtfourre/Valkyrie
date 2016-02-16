from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Order
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def order(request, order_id):
    order_view = OrderView(order_id=order_id)
    response = render(request, 'page/abstract/single-listable.html', Context(order_view.get_elements()))
    return HttpResponse(response)


class OrderView(SingleListableView):
    def __init__(self, order_id):
        current_order = Order.objects.get(pk=order_id)

        image = []

        id = [current_order.id, ]

        info = [
            ('Order Type', current_order.get_order_type_display()),
            ('Amount', current_order.amount,)
        ]

        widget = [('fragment/single-listable-widget/order-status-widget.html', current_order.order_status), ]

        id_pool = [
            ('Post ID', current_order.post_id, 'post'),
            ('Consumer ID', current_order.consumer_id, 'consumer'),
            ('Chef ID', current_order.chef_id, 'chef'),
            ('Location ID', current_order.location_id, 'location'),
            ('Billing ID', current_order.billing_id, 'billing'),
            ('Order Summary ID', current_order.order_summary_id, 'order-summary'),
        ]

        listable = []

        SingleListableView.__init__(
            self, image=image, id=id, info=info, widget=widget, id_pool=id_pool, listable=listable
        )
