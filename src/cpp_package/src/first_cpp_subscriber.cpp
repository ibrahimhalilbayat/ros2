#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class FirstCppSubscriber : public rclcpp::Node {
public:
    FirstCppSubscriber() : Node("first_cpp_subscriber") {
        subscription_ = this->create_subscription<example_interfaces::msg::String>(
            "first_cpp_topic", 10,
            [this](const example_interfaces::msg::String::SharedPtr msg) {
                callback_first_cpp_topic(msg);
            });
    }

private:
    void callback_first_cpp_topic(const example_interfaces::msg::String::SharedPtr msg) {
        RCLCPP_INFO(this->get_logger(), msg->data);
    }

    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscription_;
};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<FirstCppSubscriber>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
