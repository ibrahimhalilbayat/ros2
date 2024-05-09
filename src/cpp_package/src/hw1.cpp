#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
#include <memory>
#include <chrono>
#include <random>

using namespace std::chrono_literals;

class NumberPublisher : public rclcpp::Node
{
public:
    NumberPublisher() : Node("number_publisher")
    {
        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);

        RCLCPP_INFO(this->get_logger(), "number_publisher is created and published under number");

        timer_ = this->create_wall_timer(1s, std::bind(&NumberPublisher::publishMessage, this));
    }

private:
    void publishMessage()
    {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<int64_t> dis(0, 100);
        int64_t random_number = dis(gen);

        auto message = example_interfaces::msg::Int64();
        message.data = random_number;
        RCLCPP_INFO(this->get_logger(), "The random number is: %ld", random_number);

        publisher_->publish(message);
    }

    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
