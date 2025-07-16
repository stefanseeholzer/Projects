ActiveAdmin.register Order do
    permit_params :order_id, :customer_id, :order_date, :total_amount, :status, :created_at, :updated_at

    form do |f|
        f.semantic_errors
        f.inputs do
            f.input :customer_id, as: :select, collection: Customer.all.map { |c| [c.name, c.id] }, include_blank: true
            f.input :order_date, as: :datepicker
            f.input :total_amount
            f.input :status
        end
        f.actions
      end
end