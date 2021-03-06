from django.conf import settings
from tickets.models import Ticket
from django.contrib import messages

class Cart(object):
     
     def __init__(self, request):
          """
          Initialize the cart
          """
          self.session = request.session
          # try to get the cart form the session
          cart = self.session.get(settings.CART_SESSION_ID)
          if not cart:
               # if there's none, set an empoty one
               cart = self.session[settings.CART_SESSION_ID] = {}
          self.cart = cart
              
     def __iter__(self):
          # Iterate over the items in the cart
          ticket_ids = self.cart.keys()
          tickets = Ticket.objects.filter(id__in=ticket_ids)
          
          for ticket in tickets:
               self.cart[str(ticket.id)]['ticket'] = ticket
               
          for item in self.cart.values():
               yield item
          
     def get_total(self):
          
          return sum(int(item[1]['donation']) for item in self.cart.items())
          
     def add(self, ticket, donation=0, update=False):
          """
          Add a feature upvote to the cart 
          """
          ticket_id = str(ticket.id)
          if ticket_id not in self.cart:
               self.cart[ticket_id] = {'donation': 5}
          if update:
               self.cart[ticket_id]['donation'] = donation
          self.save()
          
  
     def save(self):
          #update the session cart
          self.session[settings.CART_SESSION_ID] = self.cart
          self.session["modified"] = True
          
     def remove(self, ticket):
          """
          Remove the ticket upvote order from the cart
          """
          ticket_id = str(ticket.id)
          if ticket_id in self.cart:
               del self.cart[ticket_id]
               self.save()
               
     def clear(self):
          
          self.session[settings.CART_SESSION_ID] = {}
          self.session["modified"] = True
          self.cart = self.session[settings.CART_SESSION_ID] 
          
     def __len__(self):
          return len(self.cart)