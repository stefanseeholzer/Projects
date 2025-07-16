class Customer < ApplicationRecord
  has_many :orders, dependent: :destroy
  belongs_to :province

  has_secure_password

  validates :name, :email, :password_digest, :address, :province, presence: true
  validates :phone_number, numericality: true
end
