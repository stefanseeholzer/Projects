class CreateContacts < ActiveRecord::Migration[7.0]
  def change
    create_table :contacts do |t|
      t.string :phone_number
      t.string :email
      t.string :hours_of_operation
      t.string :instagram
      t.string :twitter

      t.timestamps
    end
  end
end
