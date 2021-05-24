from django import conf
from django.db import models
from django.conf import settings
from cart.models import ItemCarrinho
from pagseguro.api import PagSeguroItem, PagSeguroApi
from pagseguro.signals import notificacao_recebida
import uuid


def generate_code():
    return uuid.uuid4()

class OrderManager(models.Manager):
    def create_order(self, cart):
        order = self.create(comprador=cart.user,
        valor_total=cart.subtotal)
        order.all_produtos.set(cart.produtos.all())
        return order

    def update_order(self, pagseguro_transaction):
        status = {
            '3':'Pago',
            '7':'Cancelado',
        }

        order = self.filter(id=pagseguro_transaction['reference']).first()
        if not order:
            return
        print('venda atualizada')
        
        

class Order(models.Model):
    STATUS_CHOICES = (
        (0,'Aguardando Pagamento'),
        (1,'Pagamento Aprovado'),
        (2,'Em separação'),
        (3,'Concluida'),
        (4,'Cancelada'),
    )
    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'PayPal')
    )
    id = models.UUIDField(primary_key=True, editable=False, default=generate_code)
    comprador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    payment_method = models.CharField('opção de pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20, default='deposit')
    all_produtos = models.ManyToManyField(ItemCarrinho, blank=True)
    valor_total = models.FloatField(default=0.00)

    objects = OrderManager()

    def __str__(self):
        return str(self.id) + ' '+ str(self.comprador)

    def pagseguro(self):
        pagseguro_api = PagSeguroApi(reference=self.id)
        for item in self.all_produtos.all():
            item = PagSeguroItem(
                    id=item.produto.id, 
                    description=item.produto.titulo, 
                    amount = item.produto.preco, 
                    quantity =item.qtd
        )
            pagseguro_api.add_item(item)
           
    
        return pagseguro_api.checkout()


def update_purchase_status(sender, transaction, **kwargs):
    Order.objects.update_order(transaction)


notificacao_recebida.connect(update_purchase_status)