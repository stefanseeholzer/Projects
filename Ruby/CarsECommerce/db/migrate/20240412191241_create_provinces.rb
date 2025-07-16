class CreateProvinces < ActiveRecord::Migration[7.0]
  def change
    create_table :provinces do |t|
      t.string :abbreviation
      t.float :gst
      t.float :pst

      t.timestamps
    end
  end
end
