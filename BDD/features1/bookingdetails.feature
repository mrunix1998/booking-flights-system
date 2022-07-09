Feature: Booking Details

  As a user
  I want to review my booking
  So that I can view details before the final confirmation

  Scenario Outline: User asks for Flights
    Given the <name> is signed in with <email> and <password> parameters
    When  the user asks metrics from booking table
    Then  the user view details before confirmation with <date>
    Examples:
      |    name    |           email            |    password    |               date                  |
      |  mohammad  |    mohammad331@gmail.com   |    mrunix1998  |    Mon, 21 Mar 2022 14:38:08 GMT    |
      |    nika    |    nika293@gmail.com       |    nibaka1999  |    Sat, 19 Mar 2022 14:15:55 GMT    |