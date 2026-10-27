# Isolated custom-rule integration test

These requirements apply only to fixtures/custom-rule-demo.py, a demonstration fixture, not production code.

The repository-specific contract is that the string returned by exported_job_name() must start with "ocr_". The test consumer only accepts job names with this prefix. This convention cannot be inferred from Python syntax or general coding guidelines.

If the returned string lacks this prefix, report one medium-severity finding on the return statement. Include the identifier OCR-CUSTOM-RULE-TEST-20261027 in that finding so this integration test can verify rule loading. Explain the prefix mismatch and recommend preserving the name while adding the required prefix.

If the returned string starts with "ocr_", do not report this convention as violated. Do not invent additional naming restrictions.
