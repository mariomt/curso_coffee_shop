from django.views import generic
from .forms import ProducForm

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProducForm
    