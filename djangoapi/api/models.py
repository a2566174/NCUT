from django.db import models

class ManufacturingOrder(models.Model):
    order_number = models.CharField(max_length=50, unique=True)  # 製令單號
    last_edited_date = models.DateTimeField(auto_now=True)       # 上次編輯日期
    progress = models.IntegerField(default=0)                   # 派工進度
    total_quantity = models.IntegerField(default=0)             # 總數量

class Material(models.Model):
    order = models.ForeignKey(ManufacturingOrder, on_delete=models.CASCADE, related_name='materials')
    part_name = models.CharField(max_length=50)                 # 部位名稱
    material_name = models.CharField(max_length=100)            # 材料名稱
    quantity = models.IntegerField()                            # 本批數量
    unit = models.CharField(max_length=20)                      # 單位
