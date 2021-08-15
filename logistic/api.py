from rest_framework import status, permissions, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from logistic.managers import AddressManager
from django.utils.translation import ugettext as _
from nakhll.authentications import CsrfExemptSessionAuthentication
from logistic.models import Address
from logistic.serializers import AddressSerializer
from logistic.permissions import IsAddressOwner


# class UserCartViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
#     serializer_class = CartSerializer
#     authentication_classes = [CsrfExemptSessionAuthentication, ]
#     permission_classes = [IsCartOwner, ]

#     def get_queryset(self):
#         user, guid = get_user_or_guest(self.request)
#         return CartManager.user_active_cart(user, guid)

#     def get_object(self):
#         user, guid = get_user_or_guest(self.request)
#         return CartManager.user_active_cart(user, guid)

#     @action(detail=False, methods=['POST', 'GET'], name='Send active cart to accounting')
#     def send_to_accounting(self, request):
#         # TODO: editing items in active cart when cart sent to accounting should be denied
#         # TODO: gettings diffrences is not implemented completely
#         cart = self.get_object()
#         is_differ, old, new = cart.get_diffrences()
#         if is_differ:
#             raise ValidationError('Differ')
        
#     @action(detail=False, methods=['GET'], name='View current user active cart')
#     def my(self, request):
#         cart = self.get_object()
#         serializer = self.get_serializer(cart)
#         return Response(serializer.data)
        

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = [CsrfExemptSessionAuthentication, ]
    permission_classes = [IsAddressOwner, permissions.IsAuthenticated ]
    lookup_field = 'id'

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def check_post_range(factor):
    #     src_address = factor.shop.address
    #     dst_address = factor.address


    # def calcaulate_post_price(factor):
    #     src_state = factor.shop.State
    #     src_big_city = factor.shop.BigCity
    #     src_city = factor.shop.City

    #     dst_address = factor.address
    #     dst_state = dst_address.state
    #     dst_big_city = dst_address.big_city
    #     dst_city = dst_address.city

    #     if src_state == dst_state and src_big_city == dst_big_city and src_city == dst_city:
    #         return 80000
    #     elif src_big_city == dst_big_city and src_city == dst_city:
    #         return 80000
    #     elif src_state == dst_state:
    #         return 150000
    #     else:
    #         return 200000



# class UserCartItemViewSet(viewsets.ModelViewSet):
#     def get_queryset(self):
#         user, guid = get_user_or_guest(self.request)
#         return CartItem.objects.user_cartitems(user, guid)


#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)

#         user, guid = get_user_or_guest(self.request)
#         cart_serializer = CartSerializer(CartManager.user_active_cart(user, guid))
#         headers = self.get_success_headers(cart_serializer.data)
#         return Response(cart_serializer.data, status=status.HTTP_204_NO_CONTENT, headers=headers)

#     @action(detail=True, methods=['GET'], name='Delete whole cart item')
#     def delete(self, request, pk):
#         instance = self.get_object()
#         self.perform_destroy(instance)

#         user, guid = get_user_or_guest(self.request)
#         cart_serializer = CartSerializer(CartManager.user_active_cart(user, guid))
#         headers = self.get_success_headers(cart_serializer.data)
#         return Response(cart_serializer.data, status=status.HTTP_200_OK, headers=headers)



#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     def partial_update(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)

#     @action(detail=True, methods=['GET'], name='Add item to active cart')
#     def add(self, request, pk):
#         # TODO: adding item that already in active cart should be validated with older count
#         data = {
#             'product': pk,
#             'count': 1
#         } 
#         serializer_class = self.get_serializer_class()
#         serializer = serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         user, guid = get_user_or_guest(self.request)
#         cart_serializer = CartSerializer(CartManager.user_active_cart(user, guid))
#         headers = self.get_success_headers(cart_serializer.data)
#         return Response(cart_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#     @action(detail=True, methods=['GET'], name='Remove item from active cart')
#     def remove(self, request, pk):
#         item = self.get_object()

#         if item.count == 1:
#             item.delete()
#         else:
#             item.count = item.count - 1
#             item.save()


#         user, guid = get_user_or_guest(self.request)
#         cart_serializer = CartSerializer(CartManager.user_active_cart(user, guid))
#         headers = self.get_success_headers(cart_serializer.data)
#         return Response(cart_serializer.data, status=status.HTTP_204_NO_CONTENT, headers=headers)


#     def perform_create(self, serializer):
#         ''' Add selected product to user active cart

#             Get user active cart, check if product is already in cart or not,
#             if not, create cart_item, else update that cart_item

#             Check if item exists or not, if exists, add count of that item to requested
#             count and do the validation over the product, if not procceed vaidation only
#             with requested count. It should create product in case of non-existance or
#             update in in case that is exists
#         '''
#         user, guid = get_user_or_guest(self.request)
#         product = serializer.validated_data.get('product')
#         count = serializer.validated_data.get('count')
#         active_cart = CartManager.user_active_cart(user, guid)

#         cart_item = CartItem.objects.filter(product=product, cart=active_cart).first()
#         if cart_item:
#             count = count + cart_item.count

#         if not ProductManager.is_product_available(product, count):
#             raise ValidationError(_('محصول در دسترس نیست و یا به تعداد کافی از این محصول در انبار وجود ندارد'))

#         # Make product jsonify take some time, so it should be after validation
#         product_jsonify = ProductManager.jsonify_product(product)

#         if cart_item:
#             cart_item.count = count
#             cart_item.product_last_known_state = product_jsonify
#             cart_item.save()
#         else:
#             serializer.save(cart=active_cart, product_last_known_state=product_jsonify)


#     def perform_update(self, serializer):
#         # TODO: check if permissions are correct
#         user, guid = get_user_or_guest(self.request)
#         product = serializer.validated_data.get('product')
#         count = serializer.validated_data.get('count')
#         if not ProductManager.is_product_available(product, count):
#             raise ValidationError(_('محصول در دسترس نیست و یا به تعداد کافی از این محصول در انبار وجود ندارد'))
#         product_jsonify = ProductManager.jsonify_product(product)
#         serializer.save(product_last_known_state=product_jsonify)

#     serializer_class = CartItemSerializer
#     authentication_classes = [CsrfExemptSessionAuthentication, ]
#     permission_classes = [IsCartItemOwner, ]
