ActiveAdmin.register CarModel do
    permit_params :car_model_id, :car_make_id, :name, :description, :created_at, :updated_at

    form do |f|
        f.semantic_errors
        f.inputs do
            f.input :name
            f.input :description
            f.input :car_make_id, as: :select, collection: CarMake.all.map { |cm| [cm.name, cm.id] }, include_blank: true
        end
        f.actions
    end
end