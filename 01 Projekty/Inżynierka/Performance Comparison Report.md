# Performance Comparison Report

Generated for test run: `20260719_182926`

  

This report compares the performance of different mutual TLS configurations in Istio:

  

- **mTLS 1.3 (Default)**: TLS_AES_256_GCM_SHA384 (Default Istio cipher suite)

- **mTLS 1.2 (AES-GCM)**: ECDHE-ECDSA-AES128-GCM-SHA256

- **mTLS 1.2 (ChaCha20)**: ECDHE-ECDSA-CHACHA20-POLY1305-SHA256

- **mTLS 1.2 (AES-CBC)**: ECDHE-ECDSA-AES128-SHA256 (CBC mode)

  

## TLS Verification (live sidecar stats, not just the applied CR)

  

- **mtls1.3-default**: no cipher_stats snapshot found for this run (run_all_test.sh must call capture_cipher_stats before/after this setup).

- **mtls1.2-gcm**: no cipher_stats snapshot found for this run (run_all_test.sh must call capture_cipher_stats before/after this setup).

- **mtls1.2-chacha**: no cipher_stats snapshot found for this run (run_all_test.sh must call capture_cipher_stats before/after this setup).

- **mtls1.2-cbc**: no cipher_stats snapshot found for this run (run_all_test.sh must call capture_cipher_stats before/after this setup).

  

*No cipher verification data found at all -- see run_all_test.sh changes to enable capture_cipher_stats.*

  
  

## Scenario: BASELINE

| Setup | RPS | RPS Diff | Latency Avg (ms) | Latency Diff | Latency P95 (ms) | TLS Handshakes (rate/s) | Proxy CPU (m) | App CPU (m) | Proxy Mem (MB) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **mtls1.3-default** | 7887.77 | - | 10.852 | - | 17.548 | 0.00 | 1495.5 | 2431.8 | 48.0 |
| **mtls1.2-gcm** | 7431.65 | -5.78% | 11.536 | +6.31% | 18.305 | 0.00 | 1509.1 | 2436.5 | 93.2 |
| **mtls1.2-chacha** | 7363.98 | -6.64% | 11.658 | +7.43% | 18.583 | 0.00 | 1507.9 | 2418.2 | 101.7 |
| **mtls1.2-cbc** | 7439.39 | -5.68% | 11.564 | +6.57% | 18.343 | 0.00 | 1525.0 | 2406.6 | 104.1 |

  
  

## Scenario: BASELINE-NOKEEPALIVE

| Setup | RPS | RPS Diff | Latency Avg (ms) | Latency Diff | Latency P95 (ms) | TLS Handshakes (rate/s) | Proxy CPU (m) | App CPU (m) | Proxy Mem (MB) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **mtls1.3-default** | 391.14 | - | 218.117 | - | 474.964 | 0.00 | 1500.7 | 403.9 | 89.9 |
| **mtls1.2-gcm** | 549.41 | +40.46% | 155.038 | -28.92% | 701.488 | 0.00 | 1521.6 | 317.9 | 103.6 |
| **mtls1.2-chacha** | 551.35 | +40.96% | 154.819 | -29.02% | 712.647 | 0.00 | 1498.7 | 290.9 | 106.7 |
| **mtls1.2-cbc** | 550.83 | +40.82% | 155.022 | -28.93% | 714.393 | 0.00 | 1441.3 | 300.4 | 106.1 |

  
  

## Scenario: PAYLOAD

| Setup               | RPS     | RPS Diff | Latency Avg (ms) | Latency Diff | Latency P95 (ms) | TLS Handshakes (rate/s) | Proxy CPU (m) | App CPU (m) | Proxy Mem (MB) |
| ------------------- | ------- | -------- | ---------------- | ------------ | ---------------- | ----------------------- | ------------- | ----------- | -------------- |
| **mtls1.3-default** | 1747.67 | -        | 47.332           | -            | 114.856          | 0.00                    | 1322.2        | 6476.9      | 64.4           |
| **mtls1.2-gcm**     | 1778.43 | +1.76%   | 46.493           | -1.77%       | 111.254          | 0.00                    | 1305.2        | 6696.1      | 99.6           |
| **mtls1.2-chacha**  | 1739.60 | -0.46%   | 47.599           | +0.56%       | 113.116          | 0.00                    | 1328.0        | 6300.0      | 104.2          |
| **mtls1.2-cbc**     | 1784.13 | +2.09%   | 46.434           | -1.90%       | 111.966          | 0.00                    | 1409.5        | 6610.3      | 104.0          |

  
  

## Scenario: PAYLOAD-NOKEEPALIVE

| Setup | RPS | RPS Diff | Latency Avg (ms) | Latency Diff | Latency P95 (ms) | TLS Handshakes (rate/s) | Proxy CPU (m) | App CPU (m) | Proxy Mem (MB) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **mtls1.3-default** | 478.19 | - | 177.146 | - | 325.812 | 0.00 | 1674.3 | 2518.5 | 92.6 |
| **mtls1.2-gcm** | 497.00 | +3.93% | 171.127 | -3.40% | 322.687 | 0.00 | 1617.1 | 2457.3 | 103.3 |
| **mtls1.2-chacha** | 500.60 | +4.69% | 170.138 | -3.96% | 316.019 | 0.00 | 1683.6 | 2431.0 | 107.8 |
| **mtls1.2-cbc** | 499.87 | +4.53% | 170.539 | -3.73% | 327.787 | 0.00 | 1668.4 | 2401.3 | 106.9 |

  
  

## Scenario: STRESS

| Setup               | RPS     | RPS Diff | Latency Avg (ms) | Latency Diff | Latency P95 (ms) | TLS Handshakes (rate/s) | Proxy CPU (m) | App CPU (m) | Proxy Mem (MB) |
| ------------------- | ------- | -------- | ---------------- | ------------ | ---------------- | ----------------------- | ------------- | ----------- | -------------- |
| **mtls1.3-default** | 8840.80 | -        | 48.339           | -            | 78.831           | 0.00                    | 1462.2        | 2053.4      | 82.4           |
| **mtls1.2-gcm**     | 8699.22 | -1.60%   | 49.196           | +1.77%       | 83.966           | 0.00                    | 1539.6        | 2097.9      | 101.6          |
| **mtls1.2-chacha**  | 8696.22 | -1.64%   | 49.331           | +2.05%       | 80.873           | 0.00                    | 1538.9        | 2077.1      | 104.0          |
| **mtls1.2-cbc**     | 8726.79 | -1.29%   | 49.166           | +1.71%       | 79.538           | 0.00                    | 1511.3        | 2107.3      | 103.5          |