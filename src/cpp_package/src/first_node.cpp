#include <rclcpp/rclcpp.hpp>

class LeNode : public rclcpp::Node
{
    public:
        LeNode() : Node("cpp_test"), counter_(0)
        {
            
            RCLCPP_INFO(this->get_logger(), "This is the CPP node");
            timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                            std::bind(&LeNode::timerCallback, this));


        }
    
    private:
        void timerCallback()
        {
            counter_++;
            RCLCPP_INFO(this->get_logger(), "The number: %d", counter_);
        }

        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<LeNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}