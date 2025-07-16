require "faker"
require "csv"
require "unsplash"

Car.delete_all
CarModel.delete_all
CarMake.delete_all

# AdminUser.create!(
#   email: 's@s.com',
#   password: 'password',
#   password_confirmation: 'password') if Rails.env.development?

# Car Makes
makes = ["ACME", "Hot Wheels", "Hasbro", "lego", "Micro Models"]
makes.each do |make|
  CarMake.create(
    name:        make,
    description: Faker::Lorem.sentence(word_count: 7)
  )
end
Rails.logger.info("Created makes successfully\n")

# Car Models
filename = Rails.root.join("db/data/cars.csv")

csv_data = File.read(filename)
cars = CSV.parse(csv_data, headers: true, encoding: "utf-8")

cars.each do |car|
  model_name = car["model"]
  next if CarModel.find_by(name: model_name)

  CarModel.create(
    name:        model_name,
    description: Faker::Lorem.sentence(word_count: 7),
    car_make:    CarMake.find_by(name: makes[rand(0..4)])
  )
end
Rails.logger.info("Created models successfully\n")

# Cars
filename = Rails.root.join("db/data/cars.csv")

csv_data = File.read(filename)
cars = CSV.parse(csv_data, headers: true, encoding: "utf-8")

cars.each do |car|
  name = "#{car['brand']} #{car['model']} #{Faker::Fantasy::Tolkien.character}"
  description = "#{car['year']}, from #{car['country']}, faster than a " \
                "#{Faker::Creature::Animal.name}."
  price = car["price"].to_i / 100
  price = rand(70..200) if price.zero?
  quantity = rand(1..500)

  next if Car.find_by(name:)

  model = CarModel.find_or_create_by(name: car["model"])
  vehicle = Car.create(
    name:,
    description:,
    price:,
    quantity:,
    car_model:   model
  )
  query = URI.encode_www_form_component(["toycar"].join(","))
  downloaded_image = URI.open("https://source.unsplash.com/300x300/?#{query}")
  vehicle.image.attach(io:       downloaded_image,
                       filename: "m-#{[vehicle.name,
                                       car['model']].join('-')}.jpg")
end
Rails.logger.info("Created cars successfully")
