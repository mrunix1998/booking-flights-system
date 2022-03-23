Feature: Ticket List

  As a user
  I want to be see the search results page with filters
  So that I can easily choose my desired flight

  Scenario Outline: User asks for Flights
    Given the <name> is signed in with <email> and <password> parameters
    When  the user asks <flight_id> metrics from flights table
    Then  the user sees the desired flights with <src_city> and <dst_city> and <date>
    Examples:
      |    name    |           email            |    password    |  flight_id  |   src_city   |    dst_city      |             date
      |  mohammad  |    mohammad331@gmail.com   |    mrunix1998  |      5      |   Qom        |     America      |   Tue, 01 Mar 2022 00:00:00 GMT
      |    nika    |    nika293@gmail.com       |    nibaka1999  |      2      |  AMERICA     |       Qom        |   Tue, 01 Mar 2022 00:00:00 GMT