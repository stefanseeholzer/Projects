class CreateCarMakes < ActiveRecord::Migration[7.0]
  def change
    create_table :car_makes do |t|
      t.integer :car_make_id
      t.string :name
      t.string :description

      t.timestamps
    end
  end
end
