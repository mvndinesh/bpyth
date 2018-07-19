@CALC-1958
Feature: mysecond feature
@TEST_CALC-1957
Scenario Outline: Blenders
  Given I put <thing> in a blender,
  When I switch the blender on
  Then it should transform into <other thing>

  Examples: Amphibians
    | thing           | other thing |
    | Red Tree  Frog  | mush        |

  Examples: Consumer Electronics
    | thing           | other thing |
    | iphone          | toxic waste |
    | Galaxy Nexus    | toxic waste |
