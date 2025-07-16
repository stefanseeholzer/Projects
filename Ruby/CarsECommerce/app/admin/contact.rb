ActiveAdmin.register Contact, as: "Contact Page" do
  permit_params :phone_number, :email, :hours_of_operation, :instagram, :twitter
end