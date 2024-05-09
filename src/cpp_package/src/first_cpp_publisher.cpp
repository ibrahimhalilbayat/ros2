#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class FirstCppPublisher : public rclcpp::Node
{
public:
    FirstCppPublisher() : Node("first_cpp_publisher")
    {
        publisher_ = this->create_publisher<example_interfaces::msg::String>("first_cpp_topic", 10);
        // 10 here is the queue size. It will keep up to 10 messages if some messages are late

        timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&FirstCppPublisher::publish_to_topic, this));
        RCLCPP_INFO(this->get_logger(), "Message is publishing under the topic 'first_cpp_topic'...");
    }

private:
    void publish_to_topic()
    {
        auto message = example_interfaces::msg::String();
        message.data = "One ring to rule them all";
        publisher_->publish(message);
    }

    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<FirstCppPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}