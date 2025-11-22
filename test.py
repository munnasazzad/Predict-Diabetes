def predict_diabetes():
    """
    Predicts diabetes risk based on glucose levels.
    Uses standard medical thresholds for diagnosis (ADA/WHO guidelines).
    """

    print("=" * 50)
    print("DIABETES PREDICTION SYSTEM")
    print("=" * 50)
    print("\nThis program predicts diabetes based on glucose levels.")
    print("\nNote: This is for educational purposes only.")
    print("Please consult a healthcare professional for actual diagnosis.\n")

    # Get test type
    print("Select the type of glucose test (mg/dL thresholds):")
    print("1. Fasting Plasma Glucose (FPG) - after 8+ hours fasting")
    print("2. Random Plasma Glucose (RPG) - any time of day")
    print("3. Oral Glucose Tolerance Test (OGTT) - 2 hours after glucose drink")

    while True:
        try:
            test_type = input("\nEnter your choice (1/2/3): ").strip()
            if test_type in ['1', '2', '3']:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except Exception:
            # Handles unexpected I/O errors during input
            print("Error reading input. Please try again.")

# Get glucose level
    while True:
        try:
            glucose_input = input("\nEnter glucose level in mg/dL: ").strip()
            glucose_level = float(glucose_input)

            if glucose_level < 0:
                print("Glucose level cannot be negative. Please enter a valid value.")
                continue

# Warning for extremely high values
            if glucose_level > 600:
                print("Warning: Extremely high value. Please verify the reading.")
                confirm = input("Continue with this value? (yes/no): ").strip().lower()
                if confirm not in ['yes', 'y']:
                    continue
            
            break

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception:
            print("Error reading input. Please try again.")

    # Prediction logic based on medical standards
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"\nGlucose Level: {glucose_level} mg/dL")

    status = ""
    risk = ""
    message = ""
    color = ""                                       # Placeholder for indicator

    if test_type == '1':                             # Fasting Plasma Glucose (FPG)
        print("Test Type: Fasting Plasma Glucose (FPG)")
        print("\nAnalysis:")

        if glucose_level < 100:
            status = "NORMAL"
            risk = "Low Risk"
            message = "Your fasting glucose level is normal."
            color = "✓"
        elif 100 <= glucose_level < 126:
            status = "PREDIABETES"
            risk = "Moderate Risk"
            message = "Your glucose level indicates prediabetes (impaired fasting glucose). Lifestyle changes are recommended."
            color = "!"
        else:  # >= 126
            status = "DIABETES"
            risk = "High Risk"
            message = "Your glucose level indicates diabetes. Immediate medical consultation is strongly advised."
            color = "⚠"

    elif test_type == '2':  # Random Plasma Glucose (RPG)
        print("Test Type: Random Plasma Glucose (RPG)")
        print("\nAnalysis:")

        if glucose_level < 140:
            status = "LIKELY NORMAL"
            risk = "Low Risk"
            message = "Your random glucose level appears normal. Continue monitoring."
            color = "✓"
        elif 140 <= glucose_level < 200:
            status = "ELEVATED"
            risk = "Moderate Risk"
            message = "Your glucose level is elevated. Further testing (FPG or OGTT) recommended."
            color = "!"
        else:  # >= 200
            status = "DIABETES INDICATED"
            risk = "High Risk"
            message = "Your glucose level suggests diabetes (especially if symptoms are present). Immediate medical consultation is strongly advised."
            color = "⚠"

    else:  # test_type == '3' - Oral Glucose Tolerance Test (OGTT)
        print("Test Type: Oral Glucose Tolerance Test (OGTT)")
        print("\nAnalysis:")

        if glucose_level < 140:
            status = "NORMAL"
            risk = "Low Risk"
            message = "Your 2-hour OGTT result is normal."
            color = "✓"
        elif 140 <= glucose_level < 200:
            status = "PREDIABETES"
            risk = "Moderate Risk"
            message = "Your result indicates prediabetes (impaired glucose tolerance). Lifestyle changes are recommended."
            color = "!"
        else:  # >= 200
            status = "DIABETES"
            risk = "High Risk"
            message = "Your result indicates diabetes. Immediate medical consultation is strongly advised."
            color = " "

    # Display results
    print(f"\n{color} Status: {status}")
    print(f"{color} Risk Level: {risk}")
    print(f"\n{message}")

    # Recommendations
    print("\n" + "-" * 50)
    print("RECOMMENDATIONS")
    print("-" * 50)

    if "NORMAL" in status or "LIKELY NORMAL" in status:
        print("• Maintain a healthy lifestyle")
        print("• Regular exercise and balanced diet")
        print("• Annual check-ups recommended")
    elif "PREDIABETES" in status or "ELEVATED" in status:
        print("• Consult a healthcare provider soon")
        print("• Lifestyle modifications recommended:")
        print("  - Increase physical activity")
        print("  - Adopt a healthy, balanced diet")
        print("  - Maintain healthy weight")
        print("• Regular monitoring of glucose levels")
        print("• Follow-up testing in 3-6 months")
    else:  # DIABETES
        print("• URGENT: Consult a healthcare provider immediately")
        print("• Confirm diagnosis with additional tests (e.g., HbA1c)")
        print("• May require medication or insulin therapy")
        print("• Regular blood glucose monitoring")
        print("• Diabetes management education")
        print("• Diet and exercise plan with professional guidance")

    print("\n" + "=" * 50)
    print("IMPORTANT DISCLAIMER")
    print("=" * 50)
    print("This prediction is based solely on glucose levels and")
    print("standard medical thresholds. A proper diagnosis requires:")
    print("• Multiple tests on different days")
    print("• HbA1c testing")
    print("• Complete medical evaluation")
    print("• Professional healthcare assessment")
    print("\nDO NOT use this as a substitute for medical advice!")
    print("=" * 50)

def main():
    """Main function to run the diabetes predictor."""
    while True:
        predict_diabetes()

        print("\n")
        retry = input("Would you like to check another reading? (yes/no): ").strip().lower()
        if retry not in ['yes', 'y']:
            print("\nThank you for using the Diabetes Prediction System.")
            print("Stay healthy! ")
            break
        print("\n" * 2)

if __name__ == "__main__":
    main()