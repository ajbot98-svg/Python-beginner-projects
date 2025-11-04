"""
PROJECT: coding Journey Tracker
Author: Ajay
Date: oct 31, 2025
combines: All lectures 1-4!

"""

print ("=" * 50)
print ("🚀 CODING JOURNEY TRACKER 🚀")
print ("=" * 50)

#SECTION 1: PERSONAL INFO
print ("\n📝 SECTION 1: PERSONAL INFORMATION")
print ("-" * 50)


name = input ("👤 Enter your name: ")
age = input ("🎂 Enter your age: ")
city = input ("🏙️ Enter your city: ")
education = input ("🎓 Your education:")
language = input ("Enter your favorite programming language: ")


#SECTION 2: CODING BACKGROUND
print ("\n💻 SECTION 2: CODING BACKGROUND")
print ("-" * 50)


start_date = input ("📅 When did you start learning python? (e.g., Oct 20): ")
days_learning = input ("🗓️ How many days have you been learning python? ")
hours_per_day = input ("⏰ average hours per day:")


#SECTION 3: PROGRESS TRACKING
print ("\n📊 SECTION 3: PROGRESS TRACKING")
print ("-" * 50)


lectures_completed = input ("✅ Lectures completed: ")
programs_written = input ("💾 Programs written: ")
line_of_code = input ("📝 Approximate lines of code written: ")


#SECTION 4: GOALS & MOTIVATION
print ("\n🎯 SECTION 4: GOALS & MOTIVATION")
print ("-" * 50)


goal = input ("🎯 Your main goal: ")
target_date = input ("📅 Target date (e.g., Diwali 2026): ")
why = input ("❓ Why are you learning to code? ")


# SECTION 5: FAVORITE THINGS
print ("\n🌟 SECTION 5: FAVORITE THINGS")
print ("-" * 50)


fav_language = input ("🐍 Favorite programming conecpt so far: ")
fav_project = input ("📂 Favorite project you've worked on: ")


# ================================================
# CALCULATIONS & DATA PROCESSING
# ================================================


# convert strings to numbers for calculations
age = int(age)
days_num = int(days_learning)
hours_num = float(hours_per_day)
lectures_num = int(lectures_completed)
programs_num = int(programs_written)
lines_num = int(line_of_code)


# calculate total hours
total_hours = days_num * hours_num


# calculate averages
avg_lectures_per_day = lectures_num / days_num
avg_programs_per_day = programs_num / days_num
avg_lines_per_program = lines_num / programs_num


# calculate future projections
days_until_goal = 365  # assuming 1 year
projected_lectures = lectures_num + (avg_lectures_per_day * days_until_goal)
projected_programs = programs_num + (avg_programs_per_day * days_until_goal)


# String oprations
name_length = len(name)
goal_length = len(goal)
name_upper = name.upper()


# ================================================
# GENERATE COMPLETE PROFILE
# ================================================

print ("\n")
print ("🔥" * 25)
print ("     YOUR COMPLETE CODING PROFILE ")
print ("🔥" * 25)


# personal section
print (f"\n👤 PERSONAL:")
print (f"  name: {name} ({name_length}, letters)")
print (f"  Age: {age} years old")
print (f"  Location: {city}")
print (f"  Education: {education}")


# journey section
print (f"\n💻  JOURNEY:")
print (f"   started on: {start_date}")
print (f"   days learning: {days_num} days")
print (f"   Total hours invested: {total_hours} hours")
print (f"   average hours/days: {hours_num} hours")


# progress section
print (f"\n📊 CURRENT PROGRESS:")
print (f"   ✅ lectures completed: {lectures_num}")
print (f"   ✅ programs written: {programs_num}")
print (f"   ✅ lines of code written: {lines_num} lines")
print (f"   📈 Avg lectures/day: {round(avg_lectures_per_day, 2)}")
print (f"   📈 Avg programs/day: {round(avg_programs_per_day, 2)}")
print (f"   📈 Avg lines/program: {round(avg_lines_per_program, 2)}")


# goals section
print (f"\n🎯 GOALS & MOTIVATION:")
print (f"   Main Goal: {goal}")
print (f"   Traget date: {target_date}")
print (f"   Motivation: {why}")


# Favorite section
print (f"\n🌟 FAVORITES:")
print (f"   Concept: {fav_language}")
print (f"   project: {fav_project}")


# Future Projections
print (f"\n🔮 PROJECTIONS (1 year):")
print (f"   Expected lectures: {round(projected_lectures, 0)}")
print (f"   Expected programs: {round(projected_programs, 0)}")
print (f"   Expected skill level: PROFESSIONAL! 🚀")


# motivational message
print (f"\n💪 MOTIVATIONAL MASSAGE:")
print (f"   {name_upper}, YOU'VE GOT THIS!")
print (f"   In {days_num} days, you've made incredible progress!")
print (f"   Keep going! {target_date} will be YOUR year!")


print ("\n" + "=" * 25)
print ("    PROFILE COMPLETE!")
print ("🔥" * 25)


# Final Stats Summary
print (f"\n'📌 QUICK STATS:")
print (f"    Total data points collected: 15")
print (f"    Calculations performed: 8")
print (f"    Profile sections: 6")
print (f"    Character count in goal: {goal_length}")
print (f"    Days until target date: ~{days_until_goal}")


print ("\n✅ program complete! keep coding! 💻🔥")