from sqlalchemy import Table, Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from .app import db

employee_order_rel = Table('employee_order_rel', db.Model.metadata,
    Column('employee_id', ForeignKey('employee.id')),
    Column('order_id', ForeignKey('order.id'))
)


class Supply(db.Model):
    __tablename__ = 'supply'
    id = Column(Integer, primary_key=True)
    sku = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    price_suggested = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Supply %r>' % self.sku

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Item(db.Model):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    
    supply_id = Column(Integer, ForeignKey('supply.id'))
    supply = relationship("Supply")
    
    order_id = Column(Integer, ForeignKey('order.id'))
    
    def __repr__(self):
        return '<Item %r>' % self.id


class Order(db.Model):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    
    items = relationship("Item")
    
    customer_id = Column(Integer, ForeignKey('customer.id'))
    
    employees = relationship(
        "Employee",
        secondary=employee_order_rel,
        back_populates="orders")

    def __repr__(self):
        return '<Order %r>' % self.id


class Employee(db.Model):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    salary = Column(Integer, nullable=False)
    
    orders = relationship(
        "Order",
        secondary=employee_order_rel,
        back_populates="employees")

    def __repr__(self):
        return '<Employee %r>' % self.name


class Customer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(Integer, nullable=False)
    
    orders = relationship("Order")
    quotes = relationship("Quote")
    
    def __repr__(self):
        return '<Customer %r>' % self.name


class Quote(db.Model):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True)
    
    customer_id = Column(Integer, ForeignKey('customer.id'))

    def __repr__(self):
        return '<Quote %r>' % self.id