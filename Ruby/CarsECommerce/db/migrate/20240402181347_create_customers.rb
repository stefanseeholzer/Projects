class CreateCustomers < ActiveRecord::Migration[7.0]
  def change
    create_table :customers do |t|
      t.integer :customer_id
      t.string :name
      t.string :phone_number
      t.string :address

      t.timestamps
    end
  end
end
