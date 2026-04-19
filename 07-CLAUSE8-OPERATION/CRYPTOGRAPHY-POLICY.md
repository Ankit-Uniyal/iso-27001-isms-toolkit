# Cryptography Policy
## ISO/IEC 27001:2022 — Annex A 8.24

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-POL-009
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** Chief Information Security Officer
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This policy defines NFS's requirements for the use of cryptographic controls to protect the confidentiality, integrity, and authenticity of information. It ensures cryptographic measures are applied consistently, are fit for purpose, and are managed throughout their lifecycle.

### 1.2 Scope
This policy applies to all NFS systems, applications, data stores, network communications, and portable media that process, store, or transmit information classified as Confidential or Highly Restricted. It applies to all staff, contractors, and third parties operating NFS systems.

---

## 2. Approved Cryptographic Algorithms and Standards

### 2.1 Symmetric Encryption

| Use Case | Approved Algorithm | Minimum Key Length | Notes |
|---|---|---|---|
| Data at rest (databases, files) | AES | 256-bit | AES-256-GCM preferred |
| Full disk encryption | AES | 256-bit | BitLocker (Windows), FileVault (macOS) |
| Removable media encryption | AES | 256-bit | VeraCrypt or vendor tool |
| Backup encryption | AES | 256-bit | Mandatory for all off-site backups |

### 2.2 Asymmetric Encryption and Key Exchange

| Use Case | Approved Algorithm | Minimum Key Length | Notes |
|---|---|---|---|
| TLS/HTTPS key exchange | RSA / ECDH | RSA 2048-bit / P-256 | TLS 1.2 minimum; TLS 1.3 preferred |
| Digital signatures | RSA / ECDSA | RSA 2048-bit / P-256 | SHA-256 or stronger hashing |
| Code signing | RSA / ECDSA | RSA 2048-bit | All production code must be signed |
| Email encryption / S/MIME | RSA | 2048-bit | For Highly Restricted email communications |
| SSH (remote admin) | Ed25519 / RSA | RSA 3072-bit / Ed25519 | Password-based SSH authentication prohibited |

### 2.3 Hashing

| Use Case | Approved Algorithm | Notes |
|---|---|---|
| Password storage | bcrypt / Argon2 / PBKDF2 | Minimum 12 rounds (bcrypt); MD5/SHA-1 prohibited for passwords |
| Data integrity verification | SHA-256 / SHA-3 | SHA-1 and MD5 prohibited |
| Digital signatures | SHA-256 / SHA-384 / SHA-512 | |
| HMAC | HMAC-SHA256 / HMAC-SHA512 | |

### 2.4 Transport Layer Security

| Requirement | Standard |
|---|---|
| Minimum TLS version | TLS 1.2 |
| Preferred TLS version | TLS 1.3 |
| Prohibited versions | SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1 |
| Cipher suites | Forward secrecy required (ECDHE); RC4, 3DES, NULL ciphers prohibited |
| Certificate validity | Maximum 397 days (1 year + grace); auto-renewal recommended |
| Certificate Authority | DigiCert, Sectigo, or NFS internal CA for internal services |

---

## 3. Prohibited Cryptography

The following algorithms and protocols are **prohibited** at NFS:

- DES and 3DES (Triple-DES) — deprecated
- RC4 — broken
- MD5 for security purposes (integrity or signatures)
- SHA-1 for certificates or digital signatures
- SSL 2.0 / SSL 3.0 / TLS 1.0 / TLS 1.1
- RSA keys shorter than 2048 bits
- Elliptic curves smaller than P-256 (NIST) or equivalent
- Proprietary or unvetted cryptographic algorithms
- Hard-coded encryption keys in source code

Any legacy system using prohibited cryptography must be flagged to the CISO and included in the risk register with a remediation plan.

---

## 4. Cryptographic Key Management

### 4.1 Key Generation

- All cryptographic keys must be generated using a cryptographically secure random number generator (CSPRNG)
- Keys must never be derived from predictable values (e.g., usernames, dates, dictionary words)
- Key generation must occur in a secure, controlled environment

### 4.2 Key Storage

| Key Type | Storage Method |
|---|---|
| Application encryption keys | Hardware Security Module (HSM) or cloud KMS (AWS KMS, Azure Key Vault) |
| TLS private keys | Certificate store with OS-level access controls |
| SSH private keys | User-controlled keystore; passphrase-protected |
| Code signing keys | HSM |
| Database encryption keys | Database-native KMS or external KMS |

Keys must never be stored:
- In source code or version control systems
- In plaintext files accessible to non-authorised personnel
- Alongside the data they protect

### 4.3 Key Distribution

- Keys must be distributed over secure, encrypted channels
- Key material must never be transmitted via email, messaging apps, or unencrypted protocols
- Asymmetric key pairs: public keys distributed openly; private keys never shared

### 4.4 Key Lifecycle

| Stage | Requirement |
|---|---|
| Key activation | Activate only when needed; document activation date |
| Key rotation | TLS certificates: annually; Encryption keys (at rest): annually or on suspected compromise; SSH keys: annually |
| Key revocation | Revoke immediately on: staff departure, suspected compromise, system decommission |
| Key expiry | Keys must have defined expiry dates; auto-rotation where feasible |
| Key destruction | Cryptographic erasure; overwrite key material; document destruction |

### 4.5 Key Access Control

- Access to key material restricted to authorised personnel only (least-privilege)
- Privileged key access logged in the KMS audit trail
- Dual-control required for root CA keys and master encryption keys
- Key custodians and their responsibilities documented in the Key Register

---

## 5. Certificate Management

- All TLS/SSL certificates issued for NFS public-facing services must use certificates from trusted Certificate Authorities (see Section 2.4)
- Certificate inventory maintained in the Certificate Register (tracked by IT Security)
- Automated certificate renewal configured where possible (Let's Encrypt/ACME protocol for eligible services)
- Certificate expiry monitored; alerts configured 60 days before expiry
- Wildcard certificates used only where justified; individual SAN certificates preferred
- Self-signed certificates prohibited on production systems facing external users

---

## 6. Personal Data Encryption Requirements

In support of UK GDPR obligations, the following personal data encryption requirements apply:

| Scenario | Requirement |
|---|---|
| Personal data at rest in databases | AES-256 encryption at tablespace or column level for Highly Restricted PII |
| Personal data in transit | TLS 1.2+ mandatory; TLS 1.3 for new implementations |
| Personal data on portable devices | Full disk encryption mandatory |
| Personal data in backups | AES-256 encryption mandatory |
| Personal data in email (Highly Restricted) | S/MIME or secure file transfer |

---

## 7. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| CISO | Policy ownership; approval of cryptographic standards; exception sign-off |
| IT Security Engineer | Implementation of cryptographic controls; certificate management; key rotation |
| ISMS Manager | Compliance monitoring; annual policy review |
| Development Team | Implementing approved algorithms in applications; no hard-coded keys |
| All Staff | Compliance with policy; reporting suspected key compromise |

---

## 8. Compliance and Review

Compliance with this policy is verified through:
- Annual internal audit of cryptographic controls
- Penetration testing (checks for deprecated protocols and weak ciphers)
- Automated TLS scanning (e.g., Qualys SSL Labs — target grade A or A+)
- Code reviews checking for prohibited algorithms or hard-coded keys

Non-compliant systems must be remediated within timeframes agreed with the CISO, based on risk level.

---

*Nexus Financial Services Ltd | NFS-IS-POL-009 v1.0*
*ISO/IEC 27001:2022 Annex A 8.24 — Use of cryptography*
