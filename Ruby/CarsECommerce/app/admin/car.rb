ActiveAdmin.register Car do
    permit_params :car_id, :car_model_id, :name, :description, :price, :quantity, :created_at, :updated_at, :image
    
    form do |f|
      f.semantic_errors
      f.inputs do
        f.input :name
        f.input :description
        f.input :price
        f.input :quantity
        f.input :car_model_id, as: :select, collection: CarModel.all.map { |cm| [cm.name, cm.id] }, include_blank: true
        f.input :image, as: :file, hint: f.object.image.present? ? image_tag(f.object.image, size: '125x125') : ''
      end
      f.actions
    end
end