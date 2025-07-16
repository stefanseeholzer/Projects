class CreateCarModels < ActiveRecord::Migration[7.0]
  def change
    create_table :car_models do |t|
      t.integer :car_model_id
      t.integer :car_make_id
      t.string :name
      t.string :description

      t.timestamps
    end
  end
end
