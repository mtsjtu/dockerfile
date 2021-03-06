from __future__ import print_function
import urllib2
import json
import os

IMAGES = [
    # 'addon-resizer',
    # 'addon-resizer-amd64',
    # 'addon-resizer-arm',
    # 'addon-resizer-arm64',
    # 'addon-resizer-ppc64le',
    # 'addon-resizer-s390x',
    # 'aggregator',
    # 'alpine-iptables-amd64',
    # 'alpine-iptables-arm',
    # 'alpine-iptables-arm64',
    # 'alpine-with-bash',
    # 'apparmor-loader',
    # 'busybox',
    # 'cadvisor',
    # 'cassandra',
    # 'cassandra-e2e-test',
    # 'check-metadata-concealment',
    # 'cloud-controller-manager',
    # 'cloud-controller-manager-amd64',
    # 'cloud-controller-manager-arm',
    # 'cloud-controller-manager-arm64',
    # 'cloud-controller-manager-ppc64le',
    # 'cloud-controller-manager-s390x',
    # 'cloudsql-authenticator',
    # 'cluster-autoscaler',
    # 'cluster-proportional-autoscaler-amd64',
    # 'cluster-proportional-autoscaler-arm',
    # 'cluster-proportional-autoscaler-arm64',
    # 'cluster-proportional-autoscaler-ppc64le',
    # 'clusterapi-tester',
    # 'cos-nvidia-driver-install',
    # 'cpvpa-amd64',
    # 'cuda-vector-add',
    # 'custom-metrics-stackdriver-adapter',
    # 'debian-base-amd64',
    # 'debian-base-arm',
    # 'debian-base-arm64',
    # 'debian-base-ppc64le',
    # 'debian-base-s390x',
    # 'debian-hyperkube-base-amd64',
    # 'debian-hyperkube-base-arm',
    # 'debian-hyperkube-base-arm64',
    # 'debian-hyperkube-base-ppc64le',
    # 'debian-hyperkube-base-s390x',
    # 'debian-iptables',
    # 'debian-iptables-amd64',
    # 'debian-iptables-arm',
    # 'debian-iptables-arm64',
    # 'debian-iptables-ppc64le',
    # 'debian-iptables-s390x',
    # 'defaultbackend',
    # 'defaultbackend-amd64',
    # 'defaultbackend-arm',
    # 'defaultbackend-arm64',
    # 'defaultbackend-ppc64le',
    # 'defaultbackend-s390x',
    # 'device-plugin-gpu',
    # 'dns-pod-autoscaler',
    # 'dns-rc-autoscaler',
    # 'dnsmasq',
    # 'dnsmasq-amd64',
    # 'dnsmasq-metrics-amd64',
    # 'dnsmasq-metrics-arm',
    # 'dnsmasq-metrics-arm64',
    # 'dnsmasq-metrics-ppc64le',
    # 'dnsutils',
    # 'e2e-net-amd64',
    # 'echoserver',
    # 'echoserver-amd64',
    # 'echoserver-arm',
    # 'echoserver-ppc64le',
    # 'elasticsearch',
    # 'eptest',
    # 'etcd',
    # 'etcd-amd64',
    # 'etcd-arm',
    # 'etcd-arm64',
    # 'etcd-empty-dir-cleanup',
    # 'etcd-ppc64le',
    # 'etcd-s390x',
    # 'etcd-statefulset-e2e-test',
    # 'etcd-version-monitor',
    # 'etcd-version-monitor-shyamjvs',
    # 'etcd_monitor_shyamjvs',
    # 'etcd_probe_shyamjvs',
    # 'etcd_version_monitor',
    # 'etcd_version_monitor_shyamjvs',
    # 'event-exporter',
    # 'example-dns-backend',
    # 'example-dns-frontend',
    # 'example-guestbook-php-redis',
    # 'exechealthz',
    # 'exechealthz-amd64',
    # 'exechealthz-arm',
    # 'exechealthz-arm64',
    # 'exechealthz-ppc64le',
    # 'exechealthz-s390x',
    # 'explorer',
    # 'fakegitserver',
    # 'federation-apiserver',
    # 'federation-apiserver-amd64',
    # 'federation-apiserver-arm',
    # 'federation-apiserver-arm64',
    # 'federation-apiserver-ppc64le',
    # 'federation-controller-manager',
    # 'federation-controller-manager-amd64',
    # 'federation-controller-manager-arm',
    # 'federation-controller-manager-arm64',
    # 'federation-controller-manager-ppc64le',
    # 'fetcher',
    # 'flannel-amd64',
    # 'flannel-arm',
    # 'flannel-arm64',
    # 'flannel-ppc64le',
    # 'flannel-server-helper',
    # 'fluentd-elasticsearch',
    # 'fluentd-gcp',
    # 'fluentd-journal-gcp',
    # 'fluentd-sidecar-es',
    # 'fluentd-sidecar-gcp',
    # 'galera-install',
    # 'gci-mounter',
    # 'gcsweb-amd64',
    # 'gen-swagger-docs',
    # 'git-sync',
    # 'git-sync-amd64',
    # 'github-fetcher',
    # 'github-token-counter',
    # 'github-transform',
    # 'gitolite-http',
    # 'gke-launcher',
    # 'gke-master-backup',
    # 'glbc',
    # 'google-containers-test-image',
    # 'goproxy',
    # 'guestbook',
    # 'haproxy',
    # 'healthz-server',
    # 'heapster',
    # 'heapster-amd64',
    # 'heapster-arm',
    # 'heapster-arm64',
    # 'heapster-grafana',
    # 'heapster-grafana-amd64',
    # 'heapster-grafana-arm',
    # 'heapster-grafana-arm64',
    # 'heapster-grafana-ppc64le',
    # 'heapster-grafana-s390x',
    # 'heapster-influxdb',
    # 'heapster-influxdb-amd64',
    # 'heapster-influxdb-arm',
    # 'heapster-influxdb-arm64',
    # 'heapster-influxdb-ppc64le',
    # 'heapster-influxdb-s390x',
    # 'heapster-ppc64le',
    # 'heapster-s390x',
    # 'heapster_grafana',
    # 'heapster_influxdb',
    # 'hostexec',
    # 'hpa-example',
    # 'hugo',
    # 'hyperkube',
    # 'hyperkube-amd64',
    # 'hyperkube-arm',
    # 'hyperkube-arm64',
    # 'hyperkube-ppc64le',
    # 'hyperkube-s390x',
    # 'ip-masq-agent-amd64',
    # 'ip-masq-agent-arm',
    # 'ip-masq-agent-arm64',
    # 'ip-masq-agent-ppc64le',
    # 'iperf',
    # 'jessie-dnsutils',
    # 'k8s-custom-iptables',
    # 'k8s-dns-dnsmasq-amd64',
    # 'k8s-dns-dnsmasq-arm',
    # 'k8s-dns-dnsmasq-arm64',
    # 'k8s-dns-dnsmasq-nanny-amd64',
    # 'k8s-dns-dnsmasq-nanny-arm',
    # 'k8s-dns-dnsmasq-nanny-arm64',
    # 'k8s-dns-dnsmasq-nanny-ppc64le',
    # 'k8s-dns-dnsmasq-nanny-s390x',
    # 'k8s-dns-dnsmasq-ppc64le',
    # 'k8s-dns-dnsmasq-s390x',
    # 'k8s-dns-e2e-amd64',
    # 'k8s-dns-e2e-arm',
    # 'k8s-dns-e2e-arm64',
    # 'k8s-dns-e2e-ppc64le',
    # 'k8s-dns-ginkgo-amd64',
    # 'k8s-dns-ginkgo-arm',
    # 'k8s-dns-ginkgo-arm64',
    # 'k8s-dns-ginkgo-ppc64le',
    # 'k8s-dns-kube-dns-amd64',
    # 'k8s-dns-kube-dns-arm',
    # 'k8s-dns-kube-dns-arm64',
    # 'k8s-dns-kube-dns-ppc64le',
    # 'k8s-dns-kube-dns-s390x',
    # 'k8s-dns-sidecar-amd64',
    # 'k8s-dns-sidecar-arm',
    # 'k8s-dns-sidecar-arm64',
    # 'k8s-dns-sidecar-e2e-amd64',
    # 'k8s-dns-sidecar-e2e-arm',
    # 'k8s-dns-sidecar-e2e-arm64',
    # 'k8s-dns-sidecar-e2e-ppc64le',
    # 'k8s-dns-sidecar-ppc64le',
    # 'k8s-dns-sidecar-s390x',
    # 'kibana',
    # 'kube-addon-manager',
    # 'kube-addon-manager-amd64',
    # 'kube-addon-manager-arm',
    # 'kube-addon-manager-arm64',
    # 'kube-addon-manager-ppc64le',
    # 'kube-addon-manager-s390x',
    # 'kube-aggregator',
    # 'kube-aggregator-amd64',
    # 'kube-aggregator-arm',
    # 'kube-aggregator-arm64',
    # 'kube-aggregator-ppc64le',
    # 'kube-aggregator-s390x',
    # 'kube-apiserver',
    # 'kube-apiserver-amd64',
    # 'kube-apiserver-arm',
    # 'kube-apiserver-arm64',
    # 'kube-apiserver-ppc64le',
    # 'kube-apiserver-s390x',
    # 'kube-controller-manager',
    # 'kube-controller-manager-amd64',
    # 'kube-controller-manager-arm',
    # 'kube-controller-manager-arm64',
    # 'kube-controller-manager-ppc64le',
    # 'kube-controller-manager-s390x',
    # 'kube-cross',
    # 'kube-discovery-amd64',
    # 'kube-discovery-arm',
    # 'kube-discovery-arm64',
    # 'kube-dns-perf-client-amd64',
    # 'kube-dnsmasq-amd64',
    # 'kube-dnsmasq-arm',
    # 'kube-dnsmasq-arm64',
    # 'kube-dnsmasq-ppc64le',
    # 'kube-haproxy',
    # 'kube-keepalived-vip',
    # 'kube-nethealth-amd64',
    # 'kube-proxy',
    # 'kube-proxy-amd64',
    # 'kube-proxy-arm',
    # 'kube-proxy-arm64',
    # 'kube-proxy-ppc64le',
    # 'kube-proxy-s390x',
    # 'kube-registry-proxy',
    # 'kube-scheduler',
    # 'kube-scheduler-amd64',
    # 'kube-scheduler-arm',
    # 'kube-scheduler-arm64',
    'kube-scheduler-ppc64le',
    'kube-scheduler-s390x',
    'kube-state-metrics',
    'kube-ui',
    'kube2sky',
    'kube2sky-amd64',
    'kube2sky-arm',
    'kube2sky-arm64',
    'kube2sky-ppc64le',
    'kubectl',
    'kubedash',
    'kubedns-amd64',
    'kubedns-arm',
    'kubedns-arm64',
    'kubedns-ppc64le',
    'kubekins-e2e',
    'kubekins-job-builder',
    'kubekins-test',
    'kubelet-to-gcm',
    'kubernetes-dashboard',
    'kubernetes-dashboard-amd64',
    'kubernetes-dashboard-arm',
    'kubernetes-dashboard-arm64',
    'kubernetes-dashboard-ppc64le',
    'kubernetes-dashboard-s390x',
    'kubernetes-kafka',
    'kubernetes-zookeeper',
    'leader-elector',
    'liveness',
    'loader',
    'logexp',
    'logexporter',
    'logs-generator',
    'metadata-proxy',
    'metrics-server',
    'metrics-server-amd64',
    'metrics-server-arm',
    'metrics-server-arm64',
    'metrics-server-ppc64le',
    'metrics-server-s390x',
    'mongodb-install',
    'mounttest',
    'mounttest-user',
    'mungegithub',
    'mysql-galera',
    'mysql-healthz',
    'n-way-http',
    'netexec',
    'netproxy',
    'nettest',
    'nginx',
    'nginx-ingress',
    'nginx-ingress-controller',
    'nginx-ingress-controller-amd64',
    'nginx-ingress-controller-arm',
    'nginx-ingress-controller-arm64',
    'nginx-ingress-controller-ppc64le',
    'nginx-scale',
    'nginx-slim',
    'nginx-slim-amd64',
    'nginx-slim-arm',
    'nginx-slim-arm64',
    'nginx-slim-ppc64le',
    'nginx-third-party',
    'no-snat-test-amd64',
    'no-snat-test-proxy-amd64',
    'node-conformance',
    'node-perf-dash',
    'node-problem-detector',
    'node-test',
    'node-test-amd64',
    'node-test-arm',
    'node-test-arm64',
    'nodejs-election-client',
    'non-masquerade-daemon-amd64',
    'nonewprivs',
    'pause',
    'pause-amd64',
    'pause-arm',
    'pause-arm64',
    'pause-ppc64le',
    'pause-s390x',
    'peer-finder',
    'perfdash',
    'podmaster',
    'porter',
    'portforwardtester',
    'prometheus-to-sd',
    'proxy-to-service',
    'publisher',
    'python',
    'queue-health-base',
    'queue-health-graph',
    'queue-health-poll',
    'redis',
    'redis-install',
    'redis-install-3.2.0',
    'redis-slave',
    'rescheduler',
    'rescheduler-amd64',
    'rescheduler-arm',
    'rescheduler-arm64',
    'rescheduler-ppc64le',
    'rescheduler-s390x',
    'resource_consumer',
    'rethinkdb',
    'serve_hostname',
    'serve_hostname-amd64',
    'serve_hostname-arm',
    'serve_hostname-arm64',
    'serve_hostname-ppc64le',
    'serve_hostname-s390x',
    'servicelb',
    'shame-mailer',
    'shyamjvs-logexp',
    'shyamjvs-prometheus-to-sd',
    'skydns',
    'skydns-amd64',
    'skydns-arm',
    'skydns-arm64',
    'skydns-ppc64le',
    'slo-monitor',
    'spark',
    'spark-base',
    'spark-driver',
    'spark-master',
    'spark-worker',
    'spartakus-amd64',
    'startup-script',
    'stress',
    'submit-queue',
    'test-webserver',
    'tiny-glibc-amd64',
    'tiny-glibc-arm',
    'tiny-glibc-arm64',
    'tiny-glibc-ppc64le',
    'toolbox',
    'ubuntu',
    'ubuntu-slim',
    'ubuntu-slim-amd64',
    'ubuntu-slim-arm',
    'ubuntu-slim-arm64',
    'ubuntu-slim-ppc64le',
    'update-demo',
    'volume-ceph',
    'volume-gluster',
    'volume-iscsi',
    'volume-nfs',
    'volume-rbd',
    'webhooks-publisher',
    'zeppelin',
    'zeppelin-proxy',
    'zookeeper-install',
    'zookeeper-install-3.5.0-alpha',
]


def get_tag_url(image_url):
    return 'https://gcr.io/v2/google_containers/' + image_url + '/tags/list'


for image_url in IMAGES:
    print('dealing with ' + image_url)

    raw_json = urllib2.urlopen(get_tag_url(image_url)).read()
    print(image_url+'get success')
    parsed_json = json.loads(raw_json)
    tags = parsed_json['tags']

    for tag in tags:
        filepath = os.path.join(os.getcwd(), image_url, tag, 'Dockerfile')

        try:
            docker_file = file(filepath, 'w+')

        except IOError as e:
            os.makedirs(os.path.dirname(filepath))
            docker_file = file(filepath, 'w+')

        except Exception as e:
            raise

        print('FROM gcr.io/google_containers/' + image_url + ':' + tag, file=docker_file)