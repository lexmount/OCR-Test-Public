// Standalone code fixture for organization ruleset acceptance checks.
// This module does not configure or invoke the review service.

/** Split IDs into ordered batches without changing the input array. */
function batchIds(ids, batchSize) {
  if (!Number.isSafeInteger(batchSize) || batchSize < 1) {
    throw new RangeError("batchSize must be a positive safe integer");
  }

  const batches = [];
  for (let start = 0; start < ids.length; start += batchSize) {
    batches.push(ids.slice(start, start + batchSize));
  }
  return batches;
}

module.exports = { batchIds };
