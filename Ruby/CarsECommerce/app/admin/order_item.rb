ActiveAdmin.register OrderItem do
    permit_params :order_item_id, :order_id, :car_id, :quantity, :car_price, :created_at, :updated_at
end