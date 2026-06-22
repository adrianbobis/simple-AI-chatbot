
class ResponseGenerator:

    @staticmethod
    def generate(metric, value):

        if metric == "positioning":
            return f"The selected player recorded {value} positioning events."

        if metric == "movements":
            return (
                f"Movement Statistics\n"
                f"Distance: {value['distance_m']} m\n"
                f"Max Speed: {value['max_speed_ms']} m/s\n"
                f"Average Speed: {value['avg_speed_ms']} m/s"
            )

        if metric == "good_decisions":
            if isinstance(value,list):
                lines=[]
                for i,item in enumerate(value,1):
                    ts=item["time"]
                    lines.append(f"{i}. {ts['start_s']:.2f}s → {ts['end_s']:.2f}s")
                return "Good decision timestamps\n" + "\n".join(lines)

        return str(value)
