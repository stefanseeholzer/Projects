class RemoveProvinceFromCustomers < ActiveRecord::Migration[7.0]
  def change
    remove_column :customers, :province, :string
  end
end
