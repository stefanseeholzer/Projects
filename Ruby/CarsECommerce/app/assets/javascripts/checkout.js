// HTML
{/* <div id="paypal-button-container"></div>
<input type="hidden" id="total-amount" data-total="<%= @total %>">
<script src="https://www.paypal.com/sdk/js?client-id=AWsm1zPUl4CnQuJ0zNn7Ky5Blw_f7PDzjA5cJU2i-W7IgOKRwM1RgHv8_KHiGhB-h4_BAX0n89x2taNc&currency=CAD"></script>
<%= javascript_include_tag 'checkout' %></input> */}

// Controller
// request = PayPalCheckoutSdk::Orders::OrdersCreateRequest::new
//       request.prefer('return=representation')
//       request.request_body(order_payload) # Define order_payload method to set order details
//       response = PayPalClient::client.execute(request)

//       if response.status == 'APPROVED'
//         @order.update(status: 'Paid')
    
//         flash[:notice] = "Order placed successfully!"
//       else
//         flash[:alert] = "Failed to process payment. Please try again."
//       end

// JS
paypal.Buttons({
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: document.querySelector('#total-amount').getAttribute('data-total'),
                    currency_code: 'CAD'
                }
            }]
        });
    },
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            document.getElementById('addressForm').submit();
            //document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        });
    }
}).render('#paypal-button-container');