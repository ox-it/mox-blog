Security checklist
##################

:date: 2013-04-03 10:20
:slug: security
:author: Martin Filliau
:summary: Security checklist from development to operations

Application
===========

- Run at appropriate permissions (ie. NOT root)
- Write (anonymised where appropriate) logs to provide an audit trail, keep log files secure
- Protect from:
    - SQL Injection
    - Session hijacking

System
======

- All other ports closed unless required by application // firewall
- If using SSL, all media and dynamic pages are transferred over SSL
- Make sure users have appropriate permissions (especially users for services)

Services
========

- Services should only listen on appropriate interfaces

Web server
----------

- If forwarding http:// to https:// enable strict transfer // link to documentation

SSH
---

- No root login
- No empty passwords
- Only SSH v2
- Restrict login attempts / add to iptables if needed - (fail2ban.org)
- Periodically monitor access logs (use tools where appropriate)

Database/data-layer
-------------------

- Restrict to Peer authentication (where possible)
- GRANT appropriate permissions to users
