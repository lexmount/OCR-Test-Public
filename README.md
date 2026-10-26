# OCR Public Integration Test

Public test repository for validating the Lexmount OpenCodeReview (OCR) integration.

## Purpose

Use small pull requests to verify review dispatch, review comments, and the final `ocr-review` status after an administrator configures the integration.

## Test procedure

1. Ask an administrator to configure the chosen integration for this repository.
2. Open a small pull request targeting `main`.
3. Verify that the request reaches n8n and the OCR backend.
4. Check the pull request for review comments and the final review status.
5. Push another commit to verify follow-up review behavior.

## Notes

- This repository contains test material only.
- Do not commit credentials, tokens, or private company code.
- This initial README does not configure a webhook, workflow, or merge requirement.
