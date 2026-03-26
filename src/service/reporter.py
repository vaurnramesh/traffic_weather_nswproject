from datetime import datetime
from typing import List, Dict
from src.models.evaluation import RideEvaluation

class RideReporter:
    @staticmethod
    def generate_current_report(reports: List[RideEvaluation]):
        for report in reports:
            w = report.weather
            print(f"\n📍 {report.location_name}")
            print(f"   Score: {report.analysis.score}/10 | {report.verdict}")
            print(f"   Details: {w.temp_c}°C, Wind: {w.wind_gust_kmh}km/h, Rain: {w.rain_mm}mm")
            if report.analysis.reasons:
                print(f"   ⚠️  {', '.join(report.analysis.reasons)}")

            print("\n" + "="*50)
    
    @staticmethod
    def generate_forecast_summary(forecast_matrix: Dict[str, List[RideEvaluation]], mode: str):
        title = "🌟 BEST WINDOWS" if mode == "best" else "🚩 DANGER REPORT (Avoid)"
        is_reverse = True if mode == "best" else False
        icon = "✅" if mode == "best" else "🚫"
        
        # Get the current time to filter out the past
        now = datetime.now()

        print(f"\n--- {title} ---")

        for loc, hourly_reports in forecast_matrix.items():
            print(f"\n📍 {loc}")
            
            # 1. FILTER: Only keep hours in the future
            future_reports = [
                r for r in hourly_reports 
                if datetime.fromisoformat(r.weather.timestamp) >= now
            ]
            
            if not future_reports:
                print("   No future forecast data available for today.")
                continue

            # 2. Group by Day (using the filtered list)
            days_dict = {}
            for r in future_reports:
                date_key = datetime.fromisoformat(r.weather.timestamp).strftime("%A, %b %d")
                days_dict.setdefault(date_key, []).append(r)

            for date_str, day_reports in days_dict.items():
                print(f"   --- {date_str} ---")
                sorted_reports = sorted(day_reports, key=lambda x: x.analysis.score, reverse=is_reverse)[:5]
                
                for r in sorted_reports:
                    time_label = datetime.fromisoformat(r.weather.timestamp).strftime("%H:%M")
                    print(f"   🕒 {time_label} | Score: {r.analysis.score}/10 | {r.verdict}")
                    if r.analysis.reasons:
                        print(f"      {icon} {', '.join(r.analysis.reasons)}")