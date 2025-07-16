class AddTaxesToOrderItems < ActiveRecord::Migration[7.0]
  def change
    add_column :order_items, :taxes, :float
  end
end
