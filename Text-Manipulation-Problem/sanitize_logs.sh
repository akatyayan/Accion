#!/bin/bash

INPUT_LOG="app.log"
FILTERED_LOG="filtered.log"
SANITIZED_LOG="sanitized.log"
LOWERCASE_LOG="lowercase.log"

echo "[Step 1] Filtering WARNING and ERROR logs..."
grep -E "WARNING|ERROR" "$INPUT_LOG" > "$FILTERED_LOG"


echo "[Step 2] Sanitizing IP addresses and emails..."
sed -E -e 's/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[REDACTED_IP]/g' \
       -e 's/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/[REDACTED_EMAIL]/g' \
       "$FILTERED_LOG" > "$SANITIZED_LOG"

echo "[Step 3] Converting logs to lowercase..."
tr 'A-Z' 'a-z' < "$SANITIZED_LOG" > "$LOWERCASE_LOG"

echo "[Step 4] Summary of log levels:"
awk '{print $3}' "$LOWERCASE_LOG" | sort | uniq -c

echo "Log processing complete. Check: $LOWERCASE_LOG"
