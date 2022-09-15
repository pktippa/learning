/**
 * Given an array of integers and a value, determine if there are any
 * two integers in the array whose sum is equal to the given value.
 */
// Inputs
// 1. Array of integers
// 2. Matching value

// Outputs
// 1. Boolean
import assert from "assert";

/**
 * Loop through the Array and check the difference between current value and required
 * if the value found in the tracked map, then the difference is found
 * else add to the tracked map
 *
 * if all the elements are traversed and still not found a match then return false
 */

function givenValuesInArrayCheckIfTwoNumbersSumMatched(
  arrayValues: number[],
  matched: number
) {
  const mapToTrack: { [key: number]: number } = {};
  for (let index = 0; index < arrayValues.length; index++) {
    const difference = matched - arrayValues[index];
    if (mapToTrack[difference] !== undefined) {
      return true;
    }
    mapToTrack[arrayValues[index]] = index;
  }
  return false;
}
assert.equal(givenValuesInArrayCheckIfTwoNumbersSumMatched([1, 2], 3), true);
assert.equal(givenValuesInArrayCheckIfTwoNumbersSumMatched([1, 2], 4), false);
