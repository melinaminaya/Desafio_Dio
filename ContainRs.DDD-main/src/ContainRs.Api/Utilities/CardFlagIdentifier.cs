using System.Text.RegularExpressions;

namespace ContainRs.Api.Utilities;

public class CardFlagIdentifier
{
    public static string IdentifyCardFlag(string cardNumber)
        {
            if (string.IsNullOrWhiteSpace(cardNumber))
                return "Invalid card number";

            cardNumber = cardNumber.Replace(" ", "").Replace("-", "");

            // Visa: Starts with 4, length 13 or 16
            if (Regex.IsMatch(cardNumber, @"^4[0-9]{12}(?:[0-9]{3})?$"))
                return "Visa";

            // MasterCard: Starts with 51-55 or 2221-2720, length 16
            if (Regex.IsMatch(cardNumber, @"^(5[1-5][0-9]{14}|2(2[2-9][0-9]{12}|[3-6][0-9]{13}|7[01][0-9]{12}|720[0-9]{12}))$"))
                return "MasterCard";

            // American Express: Starts with 34 or 37, length 15
            if (Regex.IsMatch(cardNumber, @"^3[47][0-9]{13}$"))
                return "American Express";

            // Discover: Starts with 6011, 622126-622925, 644-649, or 65, length 16
            if (Regex.IsMatch(cardNumber, @"^6(?:011|5[0-9]{2}|4[4-9][0-9]|22[1-9][0-9]{2}|22[2-9][0-9]{2}|622[1-9][0-9]{3}|622[2-9][0-9]{3}|6229[0-5][0-9]{2})[0-9]{12}$"))
                return "Discover";

            // JCB: Starts with 3528-3589, length 16
            if (Regex.IsMatch(cardNumber, @"^(?:2131|1800|35\d{3})\d{11}$"))
                return "JCB";

            return "Unknown card flag";
        }
}