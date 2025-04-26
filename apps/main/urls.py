from django.urls import path, include
from . import views
from .constants import ProductCategory
from .views import IndexView, ProductsView, SellerUploadView, ProductListView, AdminProductApprovalView, \
    AdminConfirmProduct, UploadClothView, UserDashboardView, CartView, ProductRentListView, CheckoutView, RecycleView, \
    ThriftView, DonateView, OrganizationDashboardView, RentalApprovalView, ProductDetailView

app_name = 'main'

product_paths = [
    path('products/', ProductsView.as_view(), name='product'),
    path("products/detail/<int:id>", ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('donate/', DonateView.as_view(), name='donate'),
    path('user/upload/donate/', UploadClothView.as_view(), {'upload_type': ProductCategory.DONATION}, name='user_upload_donate'),
    path('recycle/', RecycleView.as_view(), name='recycle'),
    path('user/upload/recycle/', UploadClothView.as_view(), {'upload_type': ProductCategory.RECYCLE}, name='user_upload_recycle'),

    path('thrift/', ThriftView.as_view(), name='thrift'),
    path('user/upload/thrift/', UploadClothView.as_view(), {'upload_type': ProductCategory.THRIFT}, name='user_upload_thrift'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<str:action>/', CartView.as_view(), name='cart_action'),
    path('cart/<str:action>/<int:item_id>/', CartView.as_view(), name='cart_action_with_id'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('user/dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('accounts/', include('apps.accounts.urls')),
    path('rent/<int:item_id>/', views.rent_item, name='rent_item'),
    path('rent_item/<int:item_id>/', views.rent_item, name='rent_item'),
    path('rental_pending/', views.rental_pending, name='rental_pending'),
    
    # Organization Dashboard URLs
    path('org/dashboard/', OrganizationDashboardView.as_view(), name='organization_dashboard'),
    path('org/confirm/<int:upload_id>/', views.confirm_cloth_upload, name='confirm_cloth_upload'),

    # Seller Dashboard URLs
    path('seller/upload/', SellerUploadView.as_view(), name='seller_upload_product'),
    path('seller/products/', ProductListView.as_view(), name='seller_product_list'),

    # Admin Dashboard URLs (removed duplicate confirm path)
    path('admin-dashboard/product-approval/', AdminProductApprovalView.as_view(), name='admin_product_approval'),
    path('admin-dashboard/confirm/<int:product_id>/', AdminConfirmProduct.as_view(), name='confirm_product'),
    path('rental-approval/', RentalApprovalView.as_view(), name='admin_rental_approval'),
      
    # Public product list and renting views (available to all users)
    path('products/', views.product_list, name='product_list'),
    path('renting/', ProductRentListView.as_view(), name='renting'),
]

urlpatterns += product_paths