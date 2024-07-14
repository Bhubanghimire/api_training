from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
  
    
    class Meta:
        model = Product
        fields = ["id","name","product_category", "description","price","cover_file","added_by"] 
        # exclude = ['keywords']