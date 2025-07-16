ActiveAdmin.register Customer do
    permit_params :customer_id, :name, :email, :phone_number, :address, :province_id, :password_digest, :created_at, :updated_at

    form do |f|
        f.semantic_errors
        f.inputs do
          f.input :name
          f.input :email
          f.input :password_digest
          f.input :phone_number
          f.input :address
          f.input :province_id, as: :select, collection: Province.all.map { |p| [p.abbreviation, p.id] }, include_blank: true
        end
        f.actions
      end
end