class CreateCars < ActiveRecord::Migration[7.0]
  def change
    create_table :cars do |t|
      t.integer :car_id
      t.integer :car_model_id
      t.string :name
      t.string :description
      t.float :price
      t.integer :quantity

      t.timestamps
    end
  end
end
