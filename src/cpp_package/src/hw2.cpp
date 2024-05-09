#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
#include <memory>

using namespace std::chrono_literals;

class NumberCounter : public rclcpp::Node
{
public:
    NumberCounter() : Node("number_counter")
    {
        RCLCPP_INFO(this->get_logger(), "number_counter is created... It publishes and subscribes");

        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number_count", 10);
        subscriber_ = this->create_subscription<example_interfaces::msg::Int64>(
            "number",
            10,
            std::bind(&NumberCounter::callbackSubscription, this, std::placeholders::_1)
        );

        timer_ = this->create_wall_timer(1s, std::bind(&NumberCounter::publishNumber, this));
    }

private:
    void publishNumber()
    {
        auto message = example_interfaces::msg::Int64();
        message.data = counter_;
        RCLCPP_INFO(this->get_logger(), "Publish the number %ld from NumberCounter", counter_);
        publisher_->publish(message);
    }

    void callbackSubscription(const example_interfaces::msg::Int64::SharedPtr receivedMessage)
    {
        RCLCPP_INFO(this->get_logger(), "Received number is: %ld", receivedMessage->data);
        counter_++;
    }

    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber_;
    rclcpp::TimerBase::SharedPtr timer_;
    int64_t counter_{0};
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberCounter>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
