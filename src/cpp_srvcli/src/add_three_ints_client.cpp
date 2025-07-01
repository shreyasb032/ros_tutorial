#include "rclcpp/rclcpp.hpp"
#include "tutorial_interfaces/srv/add_three_ints.hpp"

#include <chrono>
#include <memory>
#include <cstdlib>

using namespace std::chrono_literals;

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("add_three_ints_client");
  auto client = node->create_client<tutorial_interfaces::srv::AddThreeInts>("add_three_ints");

  auto request = std::make_shared<tutorial_interfaces::srv::AddThreeInts::Request>();
  request->a = atoll(argv[1]); // Convert the first argument to long long and assign it to request->a
  request->b = atoll(argv[2]); // Convert the second argument to long long and assign it to request->b
  request->c = atoll(argv[3]); // Convert the third argument to long long and assign it to request->c

  while (!client->wait_for_service(1s)) {
    if (!rclcpp::ok()) {
      RCLCPP_ERROR(node->get_logger(), "Interrupted while waiting for the service. Exiting.");
      return 0;
    }
    RCLCPP_INFO(node->get_logger(), "Service not available, waiting again...");
  }

  auto future_result = client->async_send_request(request); // Send the request asynchronously

  // Wait for the result
  if (rclcpp::spin_until_future_complete(node, future_result) == rclcpp::FutureReturnCode::SUCCESS) {
    RCLCPP_INFO(node->get_logger(), "Result of add_three_ints: %ld", future_result.get()->sum);
  } else {
    RCLCPP_ERROR(node->get_logger(), "Failed to call service add_three_ints");
    return 1;
  }

  rclcpp::shutdown();
  return 0;
}