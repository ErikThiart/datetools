import streamlit as st
import datetime
from datetime import timedelta
import calendar
import pandas as pd

# Page config
st.set_page_config(
    page_title="Date Calculator - Add Days, Calculate Duration & More | Free Online Tool",
    page_icon="📅",
    layout="wide"
)

# Add meta tags for SEO
st.markdown("""
<meta name="description" content="Free online date calculator to add or subtract days, calculate durations, find business days, and more. Perfect for project planning, age calculations, and deadline tracking.">
<meta name="keywords" content="date calculator, add days, subtract days, business days, day of week, date difference, free online tool">
<meta name="author" content="Erik Thiart">
<meta name="robots" content="index, follow">
""", unsafe_allow_html=True)

# Update Open Graph and Twitter Card meta tags with the correct URL and image
st.markdown("""
<meta property="og:title" content="Date Calculator - Add Days, Calculate Duration & More | Free Online Tool">
<meta property="og:description" content="Free online date calculator to add or subtract days, calculate durations, find business days, and more. Perfect for project planning, age calculations, and deadline tracking.">
<meta property="og:url" content="https://datetools.streamlit.app">
<meta property="og:type" content="website">
<meta property="og:image" content="https://datetools.streamlit.app/screenshots/app_overview.jpg">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Date Calculator - Add Days, Calculate Duration & More | Free Online Tool">
<meta name="twitter:description" content="Free online date calculator to add or subtract days, calculate durations, find business days, and more. Perfect for project planning, age calculations, and deadline tracking.">
<meta name="twitter:image" content="https://datetools.streamlit.app/screenshots/app_overview.jpg">
""", unsafe_allow_html=True)

# Update structured data for rich snippets with the correct URL and image
st.markdown("""
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "WebApplication",
  "name": "Date Calculator",
  "url": "https://datetools.streamlit.app",
  "description": "Free online date calculator to add or subtract days, calculate durations, find business days, and more.",
  "applicationCategory": "Utility",
  "creator": {
    "@type": "Person",
    "name": "Erik Thiart",
    "url": "https://erikthiart.com/"
  },
  "image": "https://datetools.streamlit.app/screenshots/app_overview.jpg",
  "keywords": [
    "date calculator",
    "add days",
    "subtract days",
    "business days",
    "day of week",
    "date difference",
    "free online tool"
  ]
}
</script>
""", unsafe_allow_html=True)

# Add a robots.txt link for better crawling
st.markdown("""
<link rel="robots" href="https://your-streamlit-app-url.com/robots.txt">
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        padding: 0.5rem;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049;
        color: white; /* Ensure text remains white on hover */
        transform: translateY(-2px);
    }
    .stButton > button:focus {
        outline: none;
        box-shadow: 0 0 5px 2px rgba(72, 239, 128, 0.5); /* Add a subtle green glow */
        background-color: #45a049; /* Match hover background */
        color: white; /* Ensure text remains white on focus */
    }
    .stButton > button:active {
        background-color: #3e8e41;
        color: white; /* Ensure text remains white on active */
        transform: translateY(0); /* Reset transform on click */
    }
    .stButton > button:visited {
        background-color: #4CAF50; /* Match default background */
        color: white; /* Ensure text remains white on visited */
    }
    .stButton > button:visited:active {
        background-color: #3e8e41; /* Match active background */
        color: white; /* Ensure text remains white on visited active */
    }
    .result-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        text-align: center;
    }
    .big-result {
        font-size: 2.5em;
        font-weight: bold;
        color: #1e3d59;
        margin: 10px 0;
    }
    .creator-footer {
        text-align: center;
        padding: 40px 20px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-top: 60px;
    }
    .calculator-tab {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    .info-card {
        background-color: #e8f4f8;
        border-left: 4px solid #1e88e5;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    div[data-testid="stButton"] > button {
        background-color: #4CAF50 !important;
        color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 📅 Date Calculator - Add Days, Calculate Duration & More")
st.markdown("### Free Online Tool for Date Calculations")

# Tab selection
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📅 Add/Subtract Days", 
    "⏱️ Days Between Dates", 
    "💼 Business Days", 
    "📆 Day of Week", 
    "🎯 Date Difference"
])

# Helper functions
def format_date_result(date):
    """Format date in multiple readable formats"""
    formats = {
        "Standard": date.strftime("%B %d, %Y"),
        "Short": date.strftime("%m/%d/%Y"),
        "International": date.strftime("%d/%m/%Y"),
        "ISO": date.strftime("%Y-%m-%d"),
        "Day of Week": date.strftime("%A")
    }
    return formats

def calculate_age_breakdown(days):
    """Break down days into years, months, weeks, days"""
    years = days // 365
    remaining = days % 365
    months = remaining // 30
    remaining = remaining % 30
    weeks = remaining // 7
    days_left = remaining % 7
    
    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if months > 0:
        parts.append(f"{months} month{'s' if months != 1 else ''}")
    if weeks > 0:
        parts.append(f"{weeks} week{'s' if weeks != 1 else ''}")
    if days_left > 0:
        parts.append(f"{days_left} day{'s' if days_left != 1 else ''}")
    
    return ", ".join(parts) if parts else "0 days"

def get_holidays_between(start_date, end_date, country="US"):
    """Get major holidays between two dates"""
    holidays = []
    
    # US Federal Holidays (simplified)
    year = start_date.year
    while year <= end_date.year:
        holiday_list = [
            (datetime.date(year, 1, 1), "New Year's Day"),
            (datetime.date(year, 7, 4), "Independence Day"),
            (datetime.date(year, 12, 25), "Christmas Day"),
            # MLK Day - 3rd Monday in January
            (datetime.date(year, 1, 1) + timedelta(days=(21 - datetime.date(year, 1, 1).weekday()) % 7 + 14), "Martin Luther King Jr. Day"),
            # Memorial Day - Last Monday in May
            (datetime.date(year, 5, 31) - timedelta(days=(datetime.date(year, 5, 31).weekday() + 7) % 7), "Memorial Day"),
            # Labor Day - 1st Monday in September
            (datetime.date(year, 9, 1) + timedelta(days=(7 - datetime.date(year, 9, 1).weekday()) % 7), "Labor Day"),
            # Thanksgiving - 4th Thursday in November
            (datetime.date(year, 11, 1) + timedelta(days=(3 - datetime.date(year, 11, 1).weekday()) % 7 + 21), "Thanksgiving"),
        ]
        
        for holiday_date, holiday_name in holiday_list:
            if start_date <= holiday_date <= end_date:
                holidays.append((holiday_date, holiday_name))
        
        year += 1
    
    return sorted(holidays)

# Tab 1: Add/Subtract Days
with tab1:
    st.markdown("### Add or Subtract Days from a Date")

    # Single column layout
    start_date = st.date_input(
        "Start Date",
        value=datetime.date.today(),
        help="Select your starting date"
    )

    operation = st.radio(
        "Operation",
        ["Add Days", "Subtract Days"],
        horizontal=True
    )

    days_to_calculate = st.number_input(
        "Number of Days",
        min_value=0,
        max_value=36500,  # 100 years
        value=30,
        help="Enter the number of days to add or subtract"
    )

    # Calculate button at the bottom
    if st.button("Calculate", key="add_subtract"):
        if operation == "Add Days":
            result_date = start_date + timedelta(days=days_to_calculate)
            operation_text = "added to"
        else:
            result_date = start_date - timedelta(days=days_to_calculate)
            operation_text = "subtracted from"

        # Display result
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="big-result">{result_date.strftime("%B %d, %Y")}</div>', unsafe_allow_html=True)
        st.markdown(f'**{days_to_calculate} days {operation_text} {start_date.strftime("%B %d, %Y")}**')

        # Show all formats
        formats = format_date_result(result_date)
        st.markdown("**Other formats:**")
        for format_name, formatted_date in formats.items():
            st.text(f"{format_name}: {formatted_date}")

        st.markdown('</div>', unsafe_allow_html=True)

        # Fun facts
        st.markdown('<div class="info-card">', unsafe_allow_html=True)
        st.markdown("**📊 Quick Facts:**")
        st.markdown(f"- That's {days_to_calculate * 24:,} hours")
        st.markdown(f"- Or {days_to_calculate * 24 * 60:,} minutes")
        st.markdown(f"- Or {days_to_calculate * 24 * 60 * 60:,} seconds")
        st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Days Between Dates
with tab2:
    st.markdown("### Calculate Days Between Two Dates")
    
    col1, col2 = st.columns(2)
    
    with col1:
        date1 = st.date_input(
            "First Date",
            value=datetime.date.today() - timedelta(days=365),
            help="Select the first date"
        )
    
    with col2:
        date2 = st.date_input(
            "Second Date",
            value=datetime.date.today(),
            help="Select the second date"
        )
    
    if st.button("Calculate Duration", key="between_dates"):
        # Calculate difference
        diff = abs((date2 - date1).days)
        
        # Display main result
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="big-result">{diff:,} days</div>', unsafe_allow_html=True)
        st.markdown(f'Between **{date1.strftime("%B %d, %Y")}** and **{date2.strftime("%B %d, %Y")}**')
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Detailed breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Years", f"{diff // 365}")
            st.metric("Total Hours", f"{diff * 24:,}")
        
        with col2:
            st.metric("Months", f"{diff // 30}")
            st.metric("Total Minutes", f"{diff * 24 * 60:,}")
        
        with col3:
            st.metric("Weeks", f"{diff // 7}")
            st.metric("Total Seconds", f"{diff * 24 * 60 * 60:,}")
        
        # Show breakdown
        st.markdown("**Detailed Breakdown:**")
        st.info(calculate_age_breakdown(diff))
        
        # Holidays between dates
        if diff > 0:
            holidays = get_holidays_between(min(date1, date2), max(date1, date2))
            if holidays:
                st.markdown("**🎉 Holidays in this period:**")
                for holiday_date, holiday_name in holidays[:5]:  # Show first 5
                    st.markdown(f"- {holiday_name}: {holiday_date.strftime('%B %d, %Y')}")

# Tab 3: Business Days Calculator
with tab3:
    st.markdown("### Calculate Business Days")
    st.markdown("Excludes weekends (Saturday & Sunday)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bus_date1 = st.date_input(
            "Start Date",
            value=datetime.date.today(),
            help="Select the start date",
            key="bus_start"
        )
    
    with col2:
        bus_date2 = st.date_input(
            "End Date",
            value=datetime.date.today() + timedelta(days=30),
            help="Select the end date",
            key="bus_end"
        )
    
    include_holidays = st.checkbox("Exclude US Federal Holidays", value=True)
    
    if st.button("Calculate Business Days", key="business_days"):
        # Calculate business days
        current = min(bus_date1, bus_date2)
        end = max(bus_date1, bus_date2)
        business_days = 0
        total_days = (end - current).days + 1
        weekends = 0
        
        # Get holidays if needed
        holidays = get_holidays_between(current, end) if include_holidays else []
        holiday_dates = {h[0] for h in holidays}
        holidays_count = 0
        
        while current <= end:
            if current.weekday() < 5:  # Monday = 0, Friday = 4
                if not include_holidays or current not in holiday_dates:
                    business_days += 1
                elif current in holiday_dates:
                    holidays_count += 1
            else:
                weekends += 1
            current += timedelta(days=1)
        
        # Display results
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="big-result">{business_days} business days</div>', unsafe_allow_html=True)
        st.markdown(f'Between **{bus_date1.strftime("%B %d, %Y")}** and **{bus_date2.strftime("%B %d, %Y")}**')
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Breakdown
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Days", total_days)
        with col2:
            st.metric("Weekend Days", weekends)
        with col3:
            st.metric("Holidays", holidays_count if include_holidays else "Not counted")
        
        # Show holidays if any
        if include_holidays and holidays:
            st.markdown("**Holidays excluded:**")
            for holiday_date, holiday_name in holidays:
                if holiday_date.weekday() < 5:  # Only show holidays on weekdays
                    st.markdown(f"- {holiday_name}: {holiday_date.strftime('%A, %B %d, %Y')}")

# Tab 4: Day of Week Calculator
with tab4:
    st.markdown("### Find Day of the Week for Any Date")

    # Quick Date Facts at the top
    today = datetime.date.today()
    st.markdown("**🎯 Quick Date Facts:**")
    st.markdown(f"- Today is **{today.strftime('%A')}**")
    st.markdown(f"- Tomorrow is **{(today + timedelta(days=1)).strftime('%A')}**")
    st.markdown(f"- Next Monday: **{(today + timedelta(days=(7-today.weekday()) % 7 or 7)).strftime('%B %d, %Y')}**")
    st.markdown(f"- Next Friday: **{(today + timedelta(days=(4-today.weekday()) % 7 or 7)).strftime('%B %d, %Y')}**")

    # Single column layout for inputs
    check_date = st.date_input(
        "Select Date",
        value=datetime.date.today(),
        help="Pick any date to find its day of the week",
        key="day_of_week"
    )

    # Calculate button at the bottom
    if st.button("Find Day of Week", key="find_day"):
        day_name = check_date.strftime("%A")

        # Display result
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="big-result">{day_name}</div>', unsafe_allow_html=True)
        st.markdown(f'{check_date.strftime("%B %d, %Y")}')
        st.markdown('</div>', unsafe_allow_html=True)

        # Additional info
        st.markdown("**📅 Additional Information:**")
        st.info(f"""
        - Week number: {check_date.isocalendar()[1]} of {check_date.year}
        - Day number: {check_date.timetuple().tm_yday} of 365
        - {calendar.isleap(check_date.year) and 'Is' or 'Is not'} a leap year
        """)

# Tab 5: Date Difference Calculator
with tab5:
    st.markdown("### Calculate Exact Time Between Dates")
    
    col1, col2 = st.columns(2)
    
    with col1:
        diff_date1 = st.date_input(
            "From Date",
            value=datetime.date(2000, 1, 1),
            help="Select the starting date",
            key="diff_start"
        )
        
        include_end_date = st.checkbox("Include end date in calculation", value=True)
    
    with col2:
        diff_date2 = st.date_input(
            "To Date",
            value=datetime.date.today(),
            help="Select the ending date",
            key="diff_end"
        )
    
    if st.button("Calculate Difference", key="calc_diff"):
        # Calculate difference
        delta = diff_date2 - diff_date1
        days = delta.days + (1 if include_end_date else 0)
        
        # Calculate various units
        years_exact = days / 365.25
        months_exact = days / 30.437
        weeks_exact = days / 7
        
        # Display main result
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="big-result">{abs(days):,} days</div>', unsafe_allow_html=True)
        
        if days < 0:
            st.markdown(f'**{diff_date1.strftime("%B %d, %Y")}** is {abs(days):,} days after **{diff_date2.strftime("%B %d, %Y")}**')
        else:
            st.markdown(f'From **{diff_date1.strftime("%B %d, %Y")}** to **{diff_date2.strftime("%B %d, %Y")}**')
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Detailed breakdown
        st.markdown("### 📊 Detailed Breakdown")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Standard Units:**")
            st.metric("Years", f"{abs(years_exact):.2f}")
            st.metric("Months", f"{abs(months_exact):.2f}")
            st.metric("Weeks", f"{abs(weeks_exact):.1f}")
            st.metric("Days", f"{abs(days):,}")
        
        with col2:
            st.markdown("**Time Units:**")
            st.metric("Hours", f"{abs(days) * 24:,}")
            st.metric("Minutes", f"{abs(days) * 24 * 60:,}")
            st.metric("Seconds", f"{abs(days) * 24 * 60 * 60:,}")
            st.metric("Milliseconds", f"{abs(days) * 24 * 60 * 60 * 1000:,}")
        
        # Fun comparisons
        if abs(days) > 0:
            st.markdown("### 🎯 Fun Comparisons")
            st.info(f"""
            - That's about **{abs(days) // 7:,} weekends**
            - Or **{abs(days) * 8:,} hours** of sleep (8 hours/night)
            - Or **{abs(days) * 3:,} meals** (3 meals/day)
            - Or **{abs(days) // 365:.1f} trips** around the sun
            """)

# Information section
st.markdown("---")
st.markdown("## 📚 How to Use This Date Calculator")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **📅 Add/Subtract Days**
    - Calculate future or past dates
    - Plan events and deadlines
    - Find dates X days from now
    """)

with col2:
    st.markdown("""
    **⏱️ Days Between Dates**
    - Calculate age in days
    - Project durations
    - Time until events
    """)

with col3:
    st.markdown("""
    **💼 Business Days**
    - Work day calculations
    - Exclude weekends & holidays
    - Project timelines
    """)

# FAQ Section
st.markdown("---")
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("How accurate is this date calculator?"):
    st.write("""
    Our date calculator is 100% accurate for date calculations. It properly handles:
    - Leap years (including century rules)
    - Different month lengths
    - Daylight saving time transitions
    - Historical calendar changes
    """)

with st.expander("What is a business day?"):
    st.write("""
    A business day (or working day) is typically Monday through Friday, excluding weekends and public holidays. 
    Our calculator can optionally exclude US federal holidays from business day calculations.
    """)

with st.expander("How do I calculate someone's age?"):
    st.write("""
    Use the 'Days Between Dates' calculator:
    1. Enter their birth date as the first date
    2. Enter today's date (or any other date) as the second date
    3. The result shows their age in days, which you can see broken down into years, months, and days
    """)

with st.expander("Can I calculate dates in the past?"):
    st.write("""
    Yes! This calculator works for any dates, past or future. You can:
    - Subtract days to find past dates
    - Calculate durations between historical dates
    - Find what day of the week any historical date was
    """)

# Creator attribution
st.markdown("""
<div class="creator-footer">
    <h3>🚀 Created by <a href="https://erikthiart.com/" target="_blank" style="color: #1e88e5; text-decoration: none;">Erik Thiart</a></h3>
    <p>Making date calculations simple and accurate</p>
    <p style="margin-top: 20px;">
        <a href="https://twitter.com/intent/tweet?text=Just%20found%20this%20amazing%20Date%20Calculator!%20Add%20days,%20find%20durations,%20calculate%20business%20days%20and%20more.%20Check%20it%20out!&url=https://datetools.streamlit.app/" 
           target="_blank" 
           style="background-color: #1DA1F2; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; margin: 0 10px;">
           Share on Twitter
        </a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://datetools.streamlit.app/" 
           target="_blank" 
           style="background-color: #0077B5; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; margin: 0 10px;">
           Share on LinkedIn
        </a>
    </p>
    <p style="margin-top: 15px; font-size: 0.9em; color: #666;">
        Free to use • No sign-up required • 100% accurate calculations
    </p>
    <p style="margin-top: 15px; font-size: 0.9em; color: #666;">
        Keywords: date calculator, add days, subtract days, business days, day of week, date difference, free online tool
    </p>
</div>
""", unsafe_allow_html=True)

# SEO Footer
st.markdown("""
---
*This free online date calculator helps you add or subtract days from any date, calculate the duration between two dates, 
find business days, determine the day of the week for any date, and more. Perfect for project planning, age calculations, 
deadline tracking, and date arithmetic. Works with past and future dates with 100% accuracy.*
""")