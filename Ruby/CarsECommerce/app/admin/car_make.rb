ActiveAdmin.register CarMake do
    permit_params :car_make_id, :name, :description, :created_at, :updated_at
end