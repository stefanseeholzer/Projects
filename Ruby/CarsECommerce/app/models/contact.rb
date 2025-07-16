class Contact < ApplicationRecord
  validates :phone_number, :email, :hours_of_operation, presence: true
end
